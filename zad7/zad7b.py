import threading
import time
import random

class Philosopher(threading.Thread):
 flag = True #is everyone finished eating?

 def __init__(self, id, leftFork, rightFork):
  threading.Thread.__init__(self)
  self.id = id
  self.leftFork = leftFork
  self.rightFork = rightFork

 def run(self):
  while(self.flag):
   # Philosopher is thinking
   time.sleep(7)
   print("Philosopher ", self.id, " is hungry.")
   self.dine()

 def dine(self):
  # if 2 forks are free, philosopher can eat
  forkL = self.leftFork
  forkR = self.rightFork
  while self.flag:
   forkL.acquire() 
   locked = forkR.acquire(False)
   if locked:
    break # right fork unavailable -> leave left fork
   forkL.release()
   print("Philosopher ", self.id, " swaps forks.")
   forkL, forkR = forkR, forkL
  else:
   return
  self.dining()
  # release 2 forks after dining
  forkR.release()
  forkL.release()

 def dining(self):
  print("Philosopher ", self.id, " starts eating")
  time.sleep(7)
  print("Philosopher ", self.id, " finishes eating and leaves to think.")

forks = []
for i in range(5):
 forks.append(threading.Lock())

philosophers = []
for k in range(5):
 philosophers.append(Philosopher(k, forks[k%5], forks[(k+1)%5]))

Philosopher.flag = True
for philosopher in philosophers:
 philosopher.start()
time.sleep(50)
Philosopher.flag = False
print("Finished.")


