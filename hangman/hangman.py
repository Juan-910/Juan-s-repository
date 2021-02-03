import random

words=['world','ball','secret','treasure','car','sport','baseball','Michael Jordan']
word= random.choice(words)

allowed_errors=5
guesses=[]
done=False

print(f"This is the hangman game!!! \n try to find the next word")
while not done:
	for letter in word:
		if letter.lower() in guesses:
			print(letter, end=" ")

		else:
			print('_',end=' ')

	print("")

	guess= input(f"Allowed errors left {allowed_errors}, Next guess: ")
	guesses.append(guess.lower())
	if guess.lower() not in word.lower():
		allowed_errors -=1
		if allowed_errors ==0:
			print(f"You lost, the word was {word}")
			break
	done= True
	for letter in word:
		if letter.lower() not in guesses:
			done= False

if done:
	print(f'You found the word! it was {word}!')
else:
	print(f"GAME OVER")