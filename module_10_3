import threading
from random import randint
from time import sleep

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range (101):
            a = randint(50, 500)
            if self.balance > 500 and self.lock.locked():
                self.lock.release()
            self.balance += a  
            print(f"Пополнение: {a}. Баланс: {self.balance}.")
            sleep(0.001)
            
        
    def take(self):
        for i in range(101):
            a = randint(50, 500)
            print(f"Запрос на {a}")
            if a <= self.balance:
                self.balance -= a
                # sleep(0.001)
                print(f"Снятие: {a}. Баланс: {self.balance}.")              
            else:
                print("Запрос отклонен, недостаточно средств")
                # sleep(0.001)
                self.lock.acquire()
            sleep(0.001)

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
