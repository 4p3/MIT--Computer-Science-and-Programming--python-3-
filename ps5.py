#problem set 5
#name: c4nn1b4l


import random
import string

#helper code

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
hand_size = 7
scrabble_letter_values = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

wordlist_filename = "F:\Programozas\Tanulos\python\mit\words.txt"

def load_words():
	#Returns a list of valid words. Words are strings of lowercase letters.
	#Depending on the size of the word list, this function may take a while to finish.
	print("Loading word list from file...")
	inFile = open(wordlist_filename, 'r', 1)
	wordlist = []
	for line in inFile:
		wordlist.append(line.strip().lower())
	print("  ", len(wordlist), "words loaded.")
	return wordlist


def get_frequency_dict(sequence):
	#Returns a dictionary where the keys are elements of the sequence and the values are integer counts,
	#for the number of times that an element is repeated in the sequence.
	#sequence: string or list
	#return: dictionary
	
	freq = {}
	for x in sequence:
		freq[x] = freq.get(x,0) + 1
	return freq


#end of helper code


#problem 1: scoring a word
def get_word_score(word, n):
	#Returns the score for a word. Assumes the word is a valid word.
	#The score for a word is the sum of the points for letters in the word, plus 50 points if all n letters are 
	#used on the first go.
	#Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.
	
	#word: string (lowercase letters)
	#returns: int >= 0
	
	score = 0
	for w in word:
		score += scrabble_letter_values[w]
	if len(word) == n:
		score += 50
	return score
	
	
def display_hand(hand):
	#Displays the letters currently in the hand. For example:
	#display_hand({'a':1, 'x':2, 'l':3, 'e':1}) Should print out something like:
	#a x x l l l e
	#The order of the letters is unimportant.
	
	#hand: dictionary (string -> int)
	
	for letter in hand.keys():
		for j in range(hand[letter]):
			print(letter, )
	print()
	
	
def deal_hand(n):
	#Returns a random hand containing n lowercase letters. At least n/3 the letters in the hand should be VOWELS.
	#Hands are represented as dictionaries. The keys are letters and the values are the number of times the
	#particular letter is repeated in that hand.
	
	#n: int >= 0
	#returns: dictionary (string -> int)
	
	hand={}
	num_vowels = n // 3
	
	for i in range(num_vowels):
		x = vowels[random.randrange(0,len(vowels))]
		hand[x] = hand.get(x, 0) + 1
		
	for i in range(num_vowels, n):
		x = consonants[random.randrange(0,len(consonants))]
		hand[x] = hand.get(x, 0) + 1
		
	return hand
	
	
#problem 2: update a hand by removing letters
def update_hand(hand, word):
	#Assumes that 'hand' has all the letters in word. In other words, this assumes that however many times
	#a letter appears in 'word', 'hand' has at least as many of that letter in it. 
	#Updates the hand: uses up the letters in the given word and returns the new hand, without those letters in it.
	#Has no side effects: does not mutate hand.

	#word: string
	#hand: dictionary (string -> int)    
	#returns: dictionary (string -> int)
	for char in word:
		if hand.get(char,0) == 0:
			return None
		elif hand.get(char, 0) > 1:
			hand[char] -= 1
		else:
			del hand[char]
	return hand
				
	
	
#problem 3: Test word validity
def is_valid_word(word, hand, word_list):
	#Returns True if word is in the word_list and is entirely composed of letters in the hand. Otherwise, returns False.
	#Does not mutate hand or word_list.
	
	#word: string
	#hand: dictionary (string -> int)
	#word_list: list of lowercase strings
	if word in word_list:
		for char in word:
			if char in hand:
				if word.count(char) > hand.get(char, 0):
					return False
			elif char not in hand:
				return False
		return True
				
	else:
		return False
	
	
	
# Problem #4: Playing a hand
def play_hand(hand, word_list):
	#Allows the user to play the given hand, as follows:
	#* The hand is displayed.
	#* The user may input a word.
	#* An invalid word is rejected, and a message is displayed asking the user to choose another word.
	#* When a valid word is entered, it uses up letters from the hand.
	#* After every valid word: the score for that word and the total score so far are displayed, the remaining letters in the hand 
	#  are displayed, and the user is asked to input another word.
	#* The sum of the word scores is displayed when the hand finishes.
	#* The hand finishes when there are no more unused letters. The user can also finish playing the hand by inputing a single
	#  period (the string '.') instead of a word.
	#* The final score is displayed.
	
	#hand: dictionary (string -> int)
	#word_list: list of lowercase strings
	solve = ""
	score = 0
	while len(hand) > 0:
		display_hand(hand)
		solve = str(input("Please enter a word, that you have formed using the letters above. You can finish by entering a single period (.) and hitting enter."))
		if solve == ".":
			return None
		elif not (is_valid_word(solve, hand, word_list)):
			print('This is not a valid word, please choose another one.')
		else:
			update_hand(hand, solve)
			print('The score for this word: ', get_word_score(solve, hand_size))
			score += get_word_score(solve, hand_size)
			print('Total score: ', score)
			print('Remaining letters in hand:')
			display_hand(hand)
			
	
	
# Problem #5: Playing a game
def play_game(word_list):
	#Allow the user to play an arbitrary number of hands.
	#	* Asks the user to input 'n' or 'r' or 'e'.
	#	* If the user inputs 'n', let the user play a new (random) hand. When done playing the hand, ask the 'n' or 'e' question again.
	#	* If the user inputs 'r', let the user play the last hand again.
	#	* If the user inputs 'e', exit the game.
	#	* If the user inputs anything else, ask them again.
	hand = deal_hand(hand_size) # random init
	while True:
		cmd = str(input('Enter n to deal a new hand, r to replay the last hand, or e to end game: '))
		if cmd == 'n':
			hand = deal_hand(hand_size)
			play_hand(hand.copy(), word_list)
			print()
		elif cmd == 'r':
			play_hand(hand.copy(), word_list)
			print()
		elif cmd == 'e':
			break
		else:
			print("Invalid command.")
	

	
#main
if __name__ == '__main__':
	word_list = load_words()
	play_game(word_list)
	
	