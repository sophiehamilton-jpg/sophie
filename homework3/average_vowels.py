# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

# Hint: You can use .isalpha() to check if a character is a letter.

def counting_vowels_and_consonants(phrase):
	sum_vowels = 0
	sum_consonants = 0
	for character in phrase:
		if character.isalpha():
			if character == "a" or character == "e" or character ==  "i" or character == "o" or character == "u":
				sum_vowels += 1
			else:
				sum_consonants += 1
	return(sum_vowels, sum_consonants)
print(counting_vowels_and_consonants("Hello there"))

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

def average_vowels_and_consonants(paragraph):
	num_vowels , num_consonants = counting_vowels_and_consonants(paragraph)
	num_sentences = 0
	for char in paragraph:
		if char in [".","?","!"]:
			num_sentences += 1
	ave_vowels = num_vowels / num_sentences
	ave_consonants = num_consonants / num_sentences
	return (num_sentences, ave_vowels, ave_consonants)


# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 

print(average_vowels_and_consonants(paragraph))
