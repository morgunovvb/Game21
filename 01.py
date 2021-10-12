import random 
random.shuffle(koloda)
koloda = [6,7,8,9,10,2,3,4,11] * 4
print('Lets play?') 
count = 0
while True: 
  choice = input('Take one card? y/n' ) 
  if choice == 'y': 
  current = koloda.pop() 
  print('Your card is %d' %current)
