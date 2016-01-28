import time
numberToCollatz = 0
def collatz(number):    
   try:
       if  (number % 2 == 0) and (number != 1):
           print(number // 2)
           numberToCollatz = number // 2
           collatz(numberToCollatz)
       elif (number % 2 == 1) and (number != 1):
           print(3 * number + 1)
           numberToCollatz = (3 * number + 1)
           collatz(numberToCollatz)
   except RecursionError:
       print('You broke it')
       time.sleep(5)
       collatz(numberToCollatz)
while True:
   try:
       collatz(int(input()))
   except ValueError:
       print('!!!ValueError. Please enter numeric characters. Thank you.!!!')
