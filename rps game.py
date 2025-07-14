import random
def play_game():
  choices=["rock", "paper", "scissors"]
  while True:
    user_choice= input("Enter a choice from Rock, Paper, Scissors or Q to quit the game").lower()
    if user_choice == "q":
      print("Thanks for playing!")
      break 
    if user_choice not in choices:
      print("Re-enter, the choice does not exists")
      continue
    
    computer_choice = random.choice(choices)
    print(f"Computer's choice is: {computer_choice}")
    if user_choice== computer_choice:
      print("It's a tie")
    elif ((user_choice=="rock" and  computer_choice=="scissors") or
    (user_choice=="scissors" and computer_choice=="paper") or 
    (user_choice=="paper" and computer_choice=="rock")):
      print("You are the winner")
    else:
      print("The computer has won so better luck next time")
  
 
play_game()   

