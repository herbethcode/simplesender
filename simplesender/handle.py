from simplesender.directory import path
from simplesender.progress import progress_bar
from simplesender.directory import path
from simplesender.arg import option



class handler(progress_bar):

     def __init__(self):
         super().__init__()
         self.options = option.run_opt()
         
     def __config__handler__(self,serv_name,serv_addr,system):
         self.server_name = serv_name
         self.system      = system
         self.serv_addr   = serv_addr
         
     def __set_info__(self,inf):
         self.if_ = inf
         
     def __is_client_need_info__(self):
         if len(self.if_) < 5:
            if 'info' in self.if_:
               return True
         return False
         
     def __send__server_info__(self,cli_sock):
         self.info = "server="+self.server_name+'\r\n'
         self.info+= "system="+self.system+'\r\n'
         self.info+= "address="+self.serv_addr+'\r\n'
         self.info = self.info.encode('utf-8')
         cli_sock.sendall(self.info)
      
     def __save_file__(self):
         
        if len(self.if_) == 0:
           return None
        self.f_info = None
        self.f_size = None
        self.f_name = None
        self.s_name = None
        
        if(len(self.if_) > 5):
           self._d_ = self.if_.split('\r\n')
           for self.__ in self._d_:
               self._ = self.__.split('===')
               if 'save' in self._[0]:
                   self.f_name = self._[1]
               if 'filesize' in self._[0]:
                   self.f_size = self._[1]
               if 'fileinfo' in self._[0]:
                   self.f_info = self._[1] 
               if 'name' in self._[0]:
                  self.s_name = self._[1]
              
        return True
        
     def __download_file__(self,cli_sock,f_name,f_size):
         try:
            self._f_ = open(f_name,'wb')
         except PermissionError:
            print("Permission denied: cannot write file in this directory\n")
            return            
         self.b_s = 10024*2
         if self.options.buffer:
            self.b_s = self.options.buffer
         print("saving in '{0}'\n\n".format(self.f_name))
         super().__set_max__(int(f_size))
         self.buff = cli_sock.recv(self.b_s)
         self.count = len(self.buff)
         while True:
               if not self.buff:
                  print("\n\nsaving complete")
                  break
               else:
                   super().__update__(int(self.count))
                   self._f_.write(self.buff)
                   self.buff = cli_sock.recv(self.b_s)
                   self.count = self.count + len(self.buff)
         
     def __close_cli_sock(self,cli_sock):
         if cli_sock:
            cli_sock.close()
         
     def __handle__(self,cli_sock, cli_addr):
         self.recv_info = cli_sock.recv(1024)
         try:
            self.decoded_data = self.recv_info.decode('utf-8')
            self.__set_info__(self.decoded_data)
         except UnicodeDecodeError:
            print("UnicodeDecodeError")
            return
         if self.__is_client_need_info__():
            self.__send__server_info__(cli_sock)
            
         elif self.__save_file__():
            if (path.__file_exist__(self.f_name) and not (self.options.overwrite)):
               print("file '",self.f_name,"' exists, overwrite ?")
               try:
                  self.ch = input("y/n? :")
               except Exception as err:
                  self.ch = 'n'
               finally:
                  if(self.ch.lower() == 'y'):
                     pass
                  else:
                    self.__close_cli_sock(cli_sock)
                    print("\n\nAborted ")
                    return 
                 
            print("Receiving file header from ",self.s_name )
            print("----------------------------------------------------------------------")
            print("File name : ",self.f_name)
            print("File size : ",path.__get_file_size_u__(float(self.f_size)))
            print("File type : ",self.f_info)
            
            self.ch = input("save? (y) or any cancel : ")
            
            if self.ch.lower() == 'y':
               self.__download_file__(cli_sock,self.f_name,self.f_size)
               self.__close_cli_sock(cli_sock)
            else:
               print("\ncancelled")
               self.__close_cli_sock(cli_sock)      
         self.__close_cli_sock(cli_sock)
         
