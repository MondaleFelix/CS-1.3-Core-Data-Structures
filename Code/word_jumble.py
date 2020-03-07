import math

# Create a histogram of counts of letters in dictionary
# Create a histogram of counts of letters in given word

# Return the word that is found in dictionary where histogram matches



with open("/usr/share/dict/words") as f:
    lines = f.read().lower()
    dictionary = lines.split('\n')



def create_histogram(str):
	d = {}
	for letter in str.lower():
		if letter in d:
			d[letter] += 1
		else:
			d[letter] = 1

	return d


def get_words_list(str):
	possible_words = []
	d = create_histogram(str)
	for word in dictionary:
		word_hist = create_histogram(word)
		if d == word_hist:
			possible_words.append(word)

	return possible_words

print(get_words_list("LAISA"))
print(get_words_list("LAURR"))
print(get_words_list("BUREEK"))
print(get_words_list("PROUOT"))