

def predicted_user_choice(history):
  return max(history, key=history.get)

def computer_move(predicted):
  if predicted=="rock":
    return "paper"
  elif predicted=="paper":
    return"scissors"
  else:
    return "rock"
    
def play_game():
  choices=["rock", "paper", "scissors"]
  user_history = {"rock": 0, "paper": 0, "scissors": 0}

  print("Play Rock-Paper-Scissors with Simple AI")
  print("Type Q to quit\n")
  
  while True:
    user_choice= input("Enter a choice from Rock, Paper, Scissors").lower()
    if user_choice == "q":
      print("Thanks for playing!")
      break 
    if user_choice not in choices:
      print("Re-enter, the choice does not exists")
      continue

    user_history[user_choice]= user_history[user_choice]+ 1
    
    predicted = predicted_user_choice(user_history)
    computer_choice = computer_move(predicted)

    print(f"Computer predicted you might choose: {predicted}")
    print(f"Computer's choice: {computer_choice}")

    if user_choice== computer_choice:
      print("It's a tie")
    elif ((user_choice=="rock" and  computer_choice=="scissors") or
    (user_choice=="scissors" and computer_choice=="paper") or 
    (user_choice=="paper" and computer_choice=="rock")):
      print("You are the winner")
    else:
      print("The computer has won so better luck next time")
      
    print("-" * 30)
  
 
play_game()   

