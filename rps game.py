import random
def play_game():
  choices=[Rock, Paper, Scissor]
  while true:
    user_choice= input("Enter a choice from Rock, Paper, Scissor or Q to quit the game").lower()
    if user_choice == q:
      print("Thanks for playing")
      break 
    for user_choice not in choices:
      print("Re-enter, the choice does not exists")
      continue
    
    computer_choice = random.choice(choices)
    print(f"Computer's choice is: {computer_choice}")
    if user_choice== computer_choice:
      print("It's a tie")
    elif ((user_choice="rock" and  computer_choice="scissor") or
    (user_choice="scissor" and computer_choice="paper") or 
    (user_choice="paper" and computer_choice="rock")):
      print("You are the winner")
else:
  print("The computer has won so better luck next time")
    
    
