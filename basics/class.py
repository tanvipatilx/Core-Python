from time import sleep
from threading import *
import threading

class Account:
    def __init__(self):
        self.lock=threading.Lock()
        self.balance=0

    def set_balance(self,balance):
        self.balance=balance

    def get_balance(self):
        return self.balance

    def deposite(self,amount):
        self.lock.acquire()
        bal=self.get_balance()
        self.set_balance(bal+amount)
        self.lock.release()

class Racing(Thread):
    def __init__(self,account,name):
        super().__init__()
        self.account=account
        self.name=name

    def run(self):
        for i in range(5):
            self.account.deposite(10)
            print(self.name , self.account.get_balance())

def main_t():
    acc=Account()
    t1=Racing(acc,"tanvi")
    t2=Racing(acc,"patil")
    t1.start()
    t2.start()

main_t()




