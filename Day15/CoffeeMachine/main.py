from random import randrange
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

item = [rock, paper, scissors]

comp = randrange(0,2)

mychoice = input('what is your choice? (0,1,2)')

print(item[comp])

print(item[int(mychoice)])

if comp == 0:
  if int(mychoice) == 1:
    print('I win')
  elif int(mychoice) == 2:
    print('I lose')
  else:
    print('Draw Game')

if comp == 1:
  if int(mychoice) == 1:
    print('Draw Game')
  elif int(mychoice) == 2:
    print('I win')
  else:
    print('I lose')

if comp == 2:
  if int(mychoice) == 1:
    print('I lose')
  elif int(mychoice) == 2:
    print('Draw Game')
  else:
    print('I win')