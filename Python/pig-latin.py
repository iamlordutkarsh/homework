#Pig Latin

# What Is Pig Latin ???

# Pig Latin is a language game or argot in which words in English are altered, usually by adding a fabricated suffix or by moving the onset or initial consonant or consonant cluster of a word to the end of the word and adding a vocalic syllable to create such a suffix.

def pig_latin(text):
	first_word = text[0]
	if first_word in 'aeiou':
		return text+'ay'
		
	elif first_word in 'AEIOU':
		return text+'ay'
				
	else:
		return text[1:]+first_word+'ay'
				
str = str(input("Enter A Word :- "))
print(" ")
print("New word :- ", pig_latin(str))