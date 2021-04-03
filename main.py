rock_0 = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
Rock'''

paper_1 = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
Paper'''

scissors_2 = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
Scissors'''

#Rock, Paper, Scisors Game
import random
choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. "))


if choose >= 3 or choose < 0:
  print("You entered an invalid number")
else:  
  comp_random = random.randint(0,2)
  my_list = [rock_0, paper_1, scissors_2]
  print(my_list[int(choose)])
  print("")
  print("Computer choose:")
  print(my_list[comp_random])

  if choose == 0 and comp_random  == 2:
      print("you win") 
  elif choose == 1 and comp_random == 0:
      print("you win")
  elif choose == 2 and comp_random == 1:
      print("you win") 
  else:
    print("you loose")    

