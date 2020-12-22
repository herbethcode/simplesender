class progress_bar:
      def __init__(self):
          self.max = None
          self.current = None
          
          
      def __set_max__(self,max_):
          self.max = max_
          
      def __update__(self,current):
          self.b_size  = 50
          self.current = current
          self.p = round(100*self.current/self.max)
          self.l = round(self.current * self.b_size/ self.max)
          self.emp = self.b_size - self.l
          print("\r|","\033[47m \033[0m"*self.l," "*self.emp,"|",self.p,"%",end="") 
        
          
