import random

#computer=random.randrange(1,20)

guess=input("Type a Number ")
if guess.isdigit():
	guess=int(guess)
	
	if guess<=0:
		print("Please type a number larger than 0 next time")
		quit()
else:
	print("Please type a number in next time")
	quit()
random_number=random.randint(0,guess)
print(random_number)
guesses=0
while True:
	guesses+=1
	user_guess=input("Enter a number: ")
	if user_guess.isdigit():
		user_guess=int(user_guess)
	else:
		print("Please type a number next time")
		continue
	
	if user_guess==random_number:
		print("You got it!")
		break
	elif user_guess>random_number:
		print("You guess smaller number the number")
	else:
		print("You guess larger the number")
print("Your Guess : ",guesses," .")
		