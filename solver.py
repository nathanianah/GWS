import random


with open('possible_words.txt') as f:
	possible = [word.strip() for word in f];

with open('allowed_words.txt') as f:
	allowed = {word.strip() for word in f};

def choose_solution():
	return random.choice(possible)

def check_guess(guess, solution):
	result = ""
	for x,y in zip(guess,solution):
		if x==y:
			result += 'G'
		elif x in solution:
			result += 'Y'
		else:
			result += 'X'
	return result

#print(choose_solution())

def play_game():
	answer = choose_solution()
	# attempt = input("Enter guess: ")
	# print(attempt)
	guesses = []
	for x in range(6):
		attempt = ""
		while attempt in guesses or attempt not in allowed:
			attempt = input("Enter guess: ")
		print(attempt, "accepted")
		guesses += [attempt]

		print(guesses)
		result = check_guess(attempt, answer)
		print (result)

		if attempt == answer:
			print("Correct")
			break
		else:
			print("Try again")
	print("Solution", answer)

play_game()