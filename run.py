import socket 
from tcp_latency import measure_latency

#creates a new socket using the given address family. 
socket_obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

#setting up the default timeout in seconds for new socket object 
socket.setdefaulttimeout(1) 


def getInput(text):
    return input(text)



def doScan(addr, port, timeout):
    port = int(port)
    finalTimeout = int(timeout) / 1000
    out = measure_latency(host=addr, port=port, runs=1, timeout=finalTimeout)
    ping = out[0]
    if not ping:
        print("Connection failed: could not reach host")
    else:
        try:
            result = socket_obj.connect_ex((addr,port)) #address and port in the tuple format 
            print("Connection success")
        except:
            print("Connection failed: port scan failed")
        socket_obj.close() 

ipaddr = getInput("Ip Address: ")
port = getInput("Port: ")
timeout = getInput("Timeout(ms): ")
doScan(ipaddr, port, timeout)