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

class Guesser:
	def __init__(self, allowed):
		self.words = [x for x in allowed]

	def possible(self, clue, last_guess, word):
		check = True
		for i,x in enumerate(clue):
			if x=='G':
				if word[i] != last_guess[i]:
					check = False
			elif x == 'Y':
				if last_guess[i] not in word or word[i]==last_guess[i]:
					check = False
			elif x == 'X':
				if last_guess[i] in word:
					check = False
		return check

	def make_guess(self, clue, last_guess):
		if not clue:
			return random.choice(self.words)
		self.words = [word for word in self.words if self.possible(clue, last_guess, word)]
		return random.choice(self.words)

#print(choose_solution())
def make_attempt(clue, tried):
	if not clue:
		candidate = [x for x in allowed]
		return random.choice(candidate)
	return random.choice(possible)


def play_game():
	answer = choose_solution()
	# attempt = input("Enter guess: ")
	# print(attempt)
	guesses = []
	ai = Guesser(allowed)
	clue = ""
	attempt = ""
	for x in range(6):
		# attempt = ""
		# while attempt in guesses or attempt not in allowed:
		# 	attempt = input("Enter guess: ")
		# print(attempt, "accepted")
		attempt = ai.make_guess(clue, attempt)
		guesses += [attempt]

		# print(guesses)
		result = check_guess(attempt, answer)
		clue = result
		# print (result)

		if attempt == answer:
			# print("Correct")
			return True, len(guesses)
			break
		# else:
			# print("Try again")
	# print("Solution", answer)
	return False, 0

correct = 0
total_tries = 0
for x in range(100):
	win, tries = play_game()
	if win:
		correct += 1
		total_tries += tries

print(correct,"guessed out of 100")
print(total_tries/correct,'average guesses')