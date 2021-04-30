import art
import game_data
import random
import replit

print(art.logo)

a = random.choice(game_data.data)
b = random.choice(game_data.data)
game_on = True
current_score = 0
while game_on==True:
  print("Compare A: "+a['name']+", "+a['description']+", from "+a['country'])
  print(art.vs)
  print("Against B: "+b['name']+", "+b['description']+", from "+b['country'])

  a_or_b = input("Who has more followers in 2021? Type 'A' or 'B': ").lower()

  if a['follower_count']>b['follower_count']:
    winner = 'a'
  elif a['follower_count']<b['follower_count']:
    winner = 'b'
  else:
    winner = "Draw"
  a=b
  b=random.choice(game_data.data)
  replit.clear()
  
  if a_or_b == winner or winner == "Draw":
    current_score+=1
    print(f"You're right! Current Score: {current_score}")
  else:
    print(f"Oops! Thats Wrong!Final Score: {current_score}")
    game_on = False


