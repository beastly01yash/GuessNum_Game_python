import random

lower_range = int(input("Enter The Lower Range: "))
upper_range = int(input("Enter The Upper Range: "))
guess = ()
count = 0
cheat = input("\nDo You Want Cheat or Not (y for yes)")

if upper_range > lower_range:
  
  random_num = random.randint(lower_range,upper_range)

  if cheat == "y":
    cheatnum1 =  random_num - random.randint(1,5)
    cheatnum2 =  random_num + random.randint(1,5)
    print(f"The Number is Between {cheatnum1} and {cheatnum2}")

  
  if upper_range - lower_range >10:
    chances = 5
  else:
    chances = 3
  print(f"You Have {chances} chances\n")
    
  while guess != random_num and chances != 0:
    
    guess = int(input("Enter The Number You Guessed: "))
    count += 1
    chances -= 1
    
    if guess > random_num:
      print("Number is Shorter Than This \n")
    elif guess < random_num:
      print("Number is Bigger Than This \n")
      
    
  if guess == random_num:
    print(f"Wohoo You Got The Number Right in {count} tries\n")
    
elif upper_range < lower_range:
  print("Please Put Larger Number in Upper Range And Smaller in Lower")
  exit()


if guess != random_num and chances == 0:
  print("Uh oh Your Chances Are Finished The Number Was ",random_num)
