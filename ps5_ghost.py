# Problem Set 5: Ghost
# Name: c4nn1b4l

import random
import string

# helper code start here
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
	#Returns a dictionary where the keys are elements of the sequence and the values are integer counts, for the number of times that
	#an element is repeated in the sequence.
	
	#sequence: string or list
	#return: dictionary
	
	freq = {}
	for x in sequence:
		freq[x] = freq.get(x,0) + 1
	return freq
	
	
#end of helper code

word_list = load_words()

def cb_valid_word(fragment, word_list):
	#Returns True if fragment could be part of a valid word. Else it returns False.
	
	#fragmen: string
	#word_list: list of lowercase strings
	for word in word_list:
		if word.startswith(fragment):
			return True
	return False
	

def is_valid_word(text, word_list):
	#return True if text is a valid word, else it returns False.
	
	#text: string
	#word_list: list of lowercase strings
	if text in word_list:
		return True
	else:
		return False
		
		
def get_players(number_of_players):
	#Gets players name, return a list containing players name
	
	#number of players: int
	
	players = []
	np = len(players)
	while np < number_of_players:
		print('Player ',(np+1),' ,')
		players.append(str(input('enter your name: ')))
		np = len(players)
	return players
	
	
def play_round(players,fragment):
	fra_temp = fragment
	for pname in players:
		print(pname,"'s turn,")
		inword = input("the letter: ")
		while inword not in string.ascii_letters or len(inword) > 1:
			inword = input("That is not a valid / single character.  Please try again!")
		fra_temp += inword
		if len(fra_temp) <= 3:
			if not cb_valid_word(fra_temp, word_list):
				print(pname, " loses because no word begins with '", fra_temp,"'!")
				players.remove(pname)
		elif len(fra_temp) > 3 and is_valid_word(fra_temp, word_list):
			print(pname, "loses because '",fra_temp,"' is a word!")
			players.remove(pname)
		else:
			if not cb_valid_word(fra_temp, word_list):
				print(pname, " loses because no word begins with '", fra_temp,"'!")
				players.remove(pname)
		print('The current word fragment is: ',fra_temp)
		fragment = fra_temp
	return (players,fragment)
	
	
def playgame():
	print('Ghost is a spoken word game in which players take turns adding letters to a growing word fragment, trying not to be the one to complete a valid word.')
	print('Each fragment must be the beginning of an actual word, and usually some minimum is set on the length of a word that counts, such as three or four letters.')
	print('The player who completes a word loses the round and earns a "letter" (as in the basketball game horse), with players being eliminated when they have been given all five letters of the word ghost.')
	number_of_players = 0
	while number_of_players == 0:
		number_of_players = int(input('Enter the number of players: '))
	players = get_players(number_of_players)
	fragment = ''
	while len(players) > 1:
		players,fragment = play_round(players,fragment)
	print(players[0],'won the game, congratulations!')
	
	
	
playgame()