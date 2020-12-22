import os
from subprocess import check_output

class path:
      def __init__(self):
          self.path = None
                    
      def __is_that_file__(self):
          if(not self.path):
             return None    
          if(not os.path.isfile(self.path)):
             return False
          return True
           
      def __get_file_size__(self):
          return os.path.getsize(self.path)
          
      def __get_file_size_u__(bytes):
          s = float(bytes)
          if s >= 1000:
             s = s * 0.001
             if s >= 1024:
                s = s / 1024
                if s >= 1024:
                    s = s / 1024
                    return "{0} (GB)".format(round(s,2))
                else:
                 return "{0} (MB)".format(round(s,2))
             else:
               return "{0} (KB)".format(round(s,2))
          else:
            return "{0} (Bytes)".format(round(s,2))
          
      def __file_exist__(filename):
          if os.path.exists(filename):
             return True
          return False
          
      def __get_file_info__(self):
         self.f_info = check_output(['file','--mime-type','-i', self.path])
         self.f_info = self.f_info.decode('utf-8')
         self.f_info = self.f_info[len(self.path)+2:]
         return self.f_info
          
      def path(self, path):
          self.path = path
          
        
