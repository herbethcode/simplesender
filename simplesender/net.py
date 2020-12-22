import socket
import sys
from simplesender.arg import option 
from subprocess import check_output

class IP:
     def __init__(self):
         self.ip_addresses = []
         self.ip_address   = None
         
     def _current_ip_(self):
          self.ip_addresses = socket.gethostbyname_ex(socket.gethostname())[2]
          for self.ip in self.ip_addresses:
              if(len(self.ip) > 0):
                 if not self.ip.startswith("127."):
                    self.ip_address = self.ip
                    return self.ip
          self.ip = check_output(['hostname', '--all-ip-addresses']).decode('utf-8')
          self.ip_address = self.ip
          return self.ip
          
          
     def r_ip(self):
          return self.ip_address
          
          
class lan(IP):
      def __init__(self):
         self.local_interfaces  = []
         self.servers_list      = []
         self.current_interface = None
         self.l_socket          = None
         super().__init__()
         self.options           = option.run_opt()
         
      def _is_connected_(self):
          '''
          
          i don't think if it is right way to prove if system 
          is connected
          
          '''
          if not super()._current_ip_():
             return False
          else:
             return True
             
      def __computer_name__(self):
          try:
             self.com_name = socket.gethostname()
          except Exception as err:
             sys.exit(str(err))
          return self.com_name
          
      def __lan_sock_open__(self):
          try:
            self.l_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
          except Exception:
            self.l_socket = None
          finally:
            return self.l_socket
            
      def __lan_sock_close__(self):
          if self.l_socket:
             self.l_socket.close()
             
      def __search_server__(self,ip):
          try:
             if (self.options.timeout):
                self.l_socket.settimeout(self.options.timeout)
             else:
                self.l_socket.settimeout(0.5)
          except OSError:
             pass
             
          try: 
             self.p = 9001
             if(self.options.port):
               self.p = self.options.port
             self.l_socket.connect((ip,self.p))
             return True
          except Exception:
             return False
             
      def __scan__(self):
          self.servers_list = []
          self.ip = super()._current_ip_()
          if not self.ip:
             sys.exit("not connected")
          
          self.oct = self.ip.split('.')

          if self.options.ip:
             print("server ip is given, scanning is disabled");
             if not self.__lan_sock_open__():
                 sys.exit("Error occured")
                 self.__lan_sock_close__()
             else:
                 if self.__search_server__(self.options.ip):
                    self.servers_list.append(self.options.ip)
                    self.__lan_sock_close__()
             return self.servers_list;
                 
          try:
            self.t_ip = self.oct[0]+'.'+self.oct[1]+'.'+self.oct[2]+'.'
          except IndexError:
            sys.exit("Ips list is empty, no ip given, connect the system to the LAN")
         
          for self.i in range(1,255):
              self.n_ip = self.t_ip+str(self.i)
              if not self.__lan_sock_open__():
                 print("Error occured")
              else:
                 if self.__search_server__(self.n_ip):
                    self.servers_list.append(self.n_ip)
                 self.__lan_sock_close__()
          self.__lan_sock_close__()
          return self.servers_list
              
      def _ip_(self):
          '''
          return currect ip address
          '''
          return super().r_ip()
          
