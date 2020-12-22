import socket
import os
import sys
from platform import system
from simplesender.net import lan
from simplesender.arg import option
from simplesender.directory import path
from simplesender.progress import progress_bar


class client(option,path, lan, progress_bar):

   def __init__(self):
       '''
       client socket variables
       
       '''
       self.cli_socket_ = None
   
       self.super_libs = super()
       self.super_libs.__init__()
       self.options   = self.super_libs.run_opt()
       if(self.options.port):
         self.port = self.options.port
       else:
         self.port = 9001
       
   def __cli_socket__(self):
       try:
          self.cli_socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
       except Exception:
          pass
       finally:
          return self.cli_socket_
          
   def __connect__(self,ip):
       try:
          self.cli_socket_.connect((ip,self.port))
          return True
       except Exception:
          return None

       
   def __retrieve_server_info__(self,ip):
       
       try:
         
          self.cli_socket_.connect((ip,self.port))
          self.cli_socket_.sendall('info'.encode('utf-8'))
          self.s_data = self.cli_socket_.recv(1024).decode('utf-8')
          return True          
       except Exception as e:
          return None
          
   def __load_server_info__(self):
       self._server_name_0 = None
       self._system_name_0 = None
       self._server_ip_0   = None
       self.arr_data = self.s_data.split('\r\n')
       for self.h in self.arr_data:
           self._h_0 = self.h.split('=')
           if 'server' in self._h_0[0]:
              self._server_name_0 = self._h_0[1]
           if 'system' in self._h_0[0]:
              self._system_name_0 = self._h_0[1]
           if 'address' in self._h_0[0]:
              self._server_ip_0 = self._h_0[1]
       
   def __send_file_info__(self,server,filename,filesize,fileinfo):
       if (self.__cli_socket__()):
          print("connecting ...\r",end="")
          if(self.__connect__(server)):
             print("connected \r",end="")
             self.t_f_name = filename.split("/")
             self.t_f_name = self.t_f_name[len(self.t_f_name)-1]
             self.inf = "save==="+self.t_f_name+"\r\n"
             self.inf+= "filesize==="+str(filesize)+"\r\n"
             self.inf+= "fileinfo==="+fileinfo+"\r\n"
             if self.options.name:
                self.inf+="name==="+self.options.name+"\r\n"
             else:
                self.inf+="name==="+self.super_libs.__computer_name__()+"\r\n"
             self.inf = self.inf.encode('utf-8')
             self.cli_socket_.sendall(self.inf)
             
          else:
            self.__cli_socket_close__()
            sys.exit("Failed to connect")
       else:
        self.__cli_socket_close__()
        sys.exit("Error ( socket.socket() )")
          
   def __send_file__(self,s):
       print("Ready to send \n")
       self._RP_ = None
       self.__set_max__(s)
       try:
         self._RP_ = open(self.options.file,'rb')
       except Exception as err:
         print(str(err))
         
       self.buff = None
       self.count = 0
       self.b_s = 10024*2
       if(self.options.buffer):
          self.b_s = self.options.buffer
       while True:
           self.buff = self._RP_.read(self.b_s)
           if not self.buff:
              print("\n\nsending complete !!")
              self.__cli_socket_close__()
              break
           else:
               try:
                  self.cli_socket_.sendall(self.buff)
                  self.count+= len(self.buff)
                  self.__update__(self.count)
               except ConnectionResetError:
                  self.__cli_socket_close__()
                  sys.exit("\n\nConnection reset by peer")
                                           
   def __clear_server_info__(self):
       self._server_name_0 = None
       self._system_name_0 = None
       self._server_ip_0   = None
   
   def __get_server_name_cli__(self):
       return self._server_name_0
       
   def __get_server_system_name_cli__(self):
       return self._system_name_0
       
   def __get_server_address_cli__(self):
       return self._server_ip_0
       
   def __cli_socket_close__(self):
       if(self.cli_socket_):
          self.cli_socket_.close()
       
   def run(self):
       self._srv_ = []
       self.super_libs.path(self.options.file)
       print("[*]scanning  ....\r", end="")
       self.target_servers = self.super_libs.__scan__()
       for self._server_ in self.target_servers:
           if (self.__cli_socket__()):
              if (self.__retrieve_server_info__(self._server_)):
                  self.__load_server_info__()
                  self.temp_ = [self.__get_server_name_cli__(),self.__get_server_system_name_cli__(),
                                self.__get_server_address_cli__()]   
                  self._srv_.append(self.temp_)
                  self.__clear_server_info__()
                  
       scrn = ds(self._srv_)
       self.target_server_ = scrn.__get__target_server__()
       if(self.target_server_ == None):
          sys.exit("rescan")
       self.__cli_socket_close__()
       if (not self.super_libs.__is_that_file__()):
          sys.exit("File '{0}' does not exist".format(self.options.file))
          
       self.file_size = self.super_libs.__get_file_size__()
       self.file_name = self.options.file
       self.file_info = self.super_libs.__get_file_info__()
       self.__send_file_info__(self.target_server_[2],self.file_name,self.file_size,self.file_info )
       self.__send_file__(self.file_size)
       
       
class ds:
     def __init__(self,servers):
         self.servers = servers
         os.system('clear')
         print("Choose the computer to send file by entering the number\n")
         
     def __get__target_server__(self):
         print("[ Computer name ]     -     [ system ]")
         print("--------------------------------------------------------------------------------")
         self.i = 1
         for self.srv in self.servers:
             print("[{0}]  {1}                  {2}".format(str(self.i),self.srv[0],self.srv[1]))
             self.i+= self.i
             
         print("\n\n")
         if(len(self.servers) == 0):
            print("No computer found")
            return None
         try:
            self.choice = input("option : ")
         except KeyboardInterrupt:
            sys.exit("\nUser interrupt")
         except EOFError:
            sys.exit("\nUser exit")
         try:
            self.choice = int(self.choice)
         except ValueError:
            sys.exit("\nonly integer required")
            
         if( (self.choice > len(self.servers) )or (self.choice < len(self.servers))):
             sys.exit("\nIndex error ")
         return self.servers[self.choice-1]
