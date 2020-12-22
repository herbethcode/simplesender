import socket
import sys
import os
from platform import system
from simplesender.arg import option
from simplesender.net import lan
from simplesender.handle import handler


class server(option, lan, handler):
    def __init__(self):
        '''
        server variables
        
        '''
        self.server_ip   = None
        self.server_port = 9001
        self.server_name = None
        
        #socket 
        self._sock_ = None
               
        '''
        load super libries
        '''
        self.super_libs = super()
        self.super_libs.__init__()
        self.options = self.super_libs.run_opt()
        
    def __socket__(self):
        try:
           self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
           self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        except Exception as err:
           pass
        finally:
           return self.sock
           
    def __scr__(self): 
        os.system("clear")
        print("Simple file sharing by herbeth | herbeth_code@gmail.com\n")
        print("Connect with this IP address: ",self.server_ip);
        print("----------------------------------------------------------------------")
       
           
    def __bind__(self):
        try:
           self.sock.bind((self.server_ip,self.server_port))
           return True
        except Exception as error:
           return None
           
    def __listen__(self):
        self.sock.listen(0)
        self.serv_name = self.super_libs.__computer_name__()
        if self.options.name:
           self.serv_name = self.options.name       
        self.__scr__()
        self.super_libs.__config__handler__(self.serv_name,self.server_ip,system())
        print("[+] Server is waiting for a client  | only one connection at time..\n")
        while self.sock:
            self.cli_sock_,self.cli_addr_ = self.sock.accept()
            self.super_libs.__handle__(self.cli_sock_,self.cli_addr_)
            
        self.sock.close()
            
    def run_server(self):
        '''
        test network connection then continue
        '''
        if not self.super_libs._is_connected_():
           sys.exit("not connected")
           
        self.server_ip = self.super_libs._ip_()
        if self.options.port:
           self.server_port = self.options.port
          
        if not self.__socket__():
           sys.exit("Error [ socket.socket() ]")
           
        if not self.__bind__():
           sys.exit("Error [ socket.bind() ] make sure the system is connected to the LAN")
           
        self.__listen__()
