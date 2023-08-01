import os 
from cronometro import *

def start(self):
    while True:
        os.system('cls')
        print(self)
        self.incremento()
        time.sleep(1)

