# Make a random pet.
import random

def animal_picker():
  animal = ["lizard", "donkey", "rock", "turtle"]
  color = ["red", "brown", "white", "green"]
  animal_choice = random.choice(animal)
  age_choice = random.randint(1, 15)
  color_choice = random.choice(color)
  weight_choice = random.uniform(10, 50)
  print(f"Your pet is a {color_choice} {animal_choice} that is {age_choice} years old and weighs {weight_choice} pounds!")
animal_picker()

answer = input("Would you like to name it? (yes, no)")
if answer == "yes":
  name = input("What would you like to name it?")
  print(f"Amazing! Your pet is now named {name.capitalize()}!")
if answer == "no":
  print(" :( I guess your pet will be unamed forever...")