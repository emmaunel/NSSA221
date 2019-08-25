#!/usr/bin/python

import os
import time
from subprocess import *
import re

def pingServer(server):
    ping = Popen(["ping", server, "-c", "3"], stdout=PIPE).stdout.read()
    #print(ping)
    for line in ping.split("\n"):
        if line[0:2] == "64":
           return True
    return False
    
def findGateway():
    res = Popen(["ip", "route"], stdout=PIPE).stdout.read()
    line = res.split("\n")[0]
    ip = re.compile(r'\d{3}.\d{1,3}.\d{1,3}.\d{1,5}')
    gateway = ip.search(line)
    test = gateway.group()
    return gateway.group()
    
def findDNServer():
    servers = []
    conf = open("/etc/resolv.conf", "r")
    for line in conf:
        if line[0:10] == "nameserver":
            servers.append(line.split()[1])
    return servers

def pingDNServer():
    servers = findDNServer()
    success = []
    for server in servers:
        if pingServer(server):
            success.append(server)
            
    if len(servers) == len(success):
        return True
    return False
    
def pingGateway():
    server = findGateway()
    if server:
        return pingServer(server)
    return False
    
def pingRemote():
    return pingServer("8.8.8.8")
    
    
def timer(n):
    while n > 0:
        print("          " + str(n))
        n -= 1
    if n == 0:
        return

if __name__ == '__main__':
    os.system("clear")
    print("***Beginning Test***")
    timer(5)
    print("Your default gateway is " + findGateway() + ".")
    result = "SUCCESSFUL!" if pingGateway() else "FAILURE!"
    print("Connection to default gateway is " + result)
    result = "SUCCESSFUL!" if pingRemote() else "FAILURE!"
    print("Remote Connection " + result)
    result = "SUCCESSFUL!" if pingDNServer() else "FAILURE!"
    print("DNS resolution " + result)
    print("*** Test Complete. ***")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
