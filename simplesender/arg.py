import argparse 
import sys
    

class option:
      def __init__(self):
          self.parser = argparse.ArgumentParser(add_help=False )
          self.parser.add_argument('-h', '--help', action="store_true",help=" ")
          self.parser.add_argument('-r', '--recieve', action="store_true",help=" ")
          self.parser.add_argument('-n','--name',action="store") 
          self.parser.add_argument('-i','--ip',action="store") 
          self.parser.add_argument('-p','--port', type=int,action="store") 
          self.parser.add_argument('-f','--file',action="store") 
          self.parser.add_argument('-b','--buffer',type=int,action="store") 
          self.parser.add_argument('-t','--timeout',type=int,action="store") 
          self.parser.add_argument('-o', '--overwrite', action="store_true",help=" ")
          self.options = self.parser.parse_args()
          
      def __help__(self):
          self.usage = "\n Simplesender 0.01 - 2020 - Herbeth Norasco\n"
          self.usage+= " herbeth.code@gmail.com"
          self.usage+= "\n\n Usage: simpletransfer.py [ OPTIONS ]"
          self.usage+="\n\n options:\n"
          self.usage+="        -h  --help      :  print this and exit\n"
          self.usage+="        -r  --receive   :  set receiving mode\n"
          self.usage+="        -n  --name      :  server name\n"
          self.usage+="        -p  --port      :  service port, this require root permition\n"
          self.usage+="        -f  --file      :  file to send \n"
          self.usage+="        -b  --buffer    :  buffer size\n"
          self.usage+="        -t  --timeout   :  socket timeout in secs\n"
          self.usage+="        -o  --overwrite :  overwrite existing file\n"
          self.usage+="        -i  --ip        :  server ip address\n"
          self.usage+="\n\n  examples: simpletranfer -r\n"
          self.usage+="            ssender -r -n name -o \n"
          self.usage+="            ssender -f filename -n name  \n\n"
          return self.usage
          
      def run_opt(self):
          if self.options.help:
             sys.exit(self.__help__())
          return self.options
