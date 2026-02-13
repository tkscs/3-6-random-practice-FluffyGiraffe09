import random
def spin_twister_spinner():
  color = ["red", "green", "yellow", "blue"]
  side = ["left", "right"]
  appendage = ["hand", "foot"]
  color_choice = random.choice(color)
  side_choice = random.choice(side)
  appendage_choice = random.choice(appendage)
  return (f"Put your {side_choice} {appendage_choice} on {color_choice}")
for _ in range(10):
  print(spin_twister_spinner())