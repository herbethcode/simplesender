import sys
import platform
from simplesender import arg
from simplesender import server
from simplesender import client

def run():
   try:
    opt = arg.option()
    opt = opt.run_opt()
        
    if opt.recieve:
       serv = server.server()
       serv.run_server()
       
    else:
      cli = client.client()
      cli.run()
   except KeyboardInterrupt:
      sys.exit("\nKeyboardInterrupt")
