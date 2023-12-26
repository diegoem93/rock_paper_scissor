import random

options = ('rock', 'paper', 'scissor')
computer_wins = 0
user_wins = 0
rounds = 1 

print('Welcome to rock, paper, scissor game. Please choose the number of rounds that you want to play (it must be an odd number) and after that you have to choose your option to play vs the computer.')
while True:
  total_rounds = int(input('Choose the number of rounds to play: '))
  if total_rounds % 2 == 0:
    print('It must be an odd number')
    continue
  elif total_rounds > 10:
    print('Select a number smaller than 10')
    continue
  else:
    break

while True:
  
  print('*' * 10)
  print('ROUND ', rounds)
  print('*' * 10)

  print(f'So far the results are: Computer  {computer_wins} User {user_wins}')
  
  user_option = input('rock, paper o scissor => ').lower()
  if user_option not in options:
    print('This is not a valid option')
    continue
  computer_option = random.choice(options).lower()
    

  print('User option => ', user_option)
  print('Computer option => ', computer_option)

  if user_option == computer_option:
    print('Tie')
  elif user_option == 'rock':
    if computer_option == 'scissor':
      print('You Win')
      user_wins += 1
    else:
      print('You Lose')
      computer_wins += 1
  elif user_option == 'paper':
    if computer_option == 'rock':
      print('You Win')
      user_wins += 1
    else:
      print('You Lose')
      computer_wins += 1
  elif user_option == 'scissor': 
    if computer_option == 'paper':
      print('You Win')
      user_wins += 1
    else:
      print('You Lose')
      computer_wins += 1
  if computer_wins == float((total_rounds / 2)) + 0.5:
    print(f'The computer won. The results are: User {user_wins} Computer {computer_wins}')
    break

  if user_wins == float((total_rounds / 2)) + 0.5:
    print(f'You won, congrats!. The results are: User {user_wins} Computer {computer_wins}')
    break
  
  rounds += 1