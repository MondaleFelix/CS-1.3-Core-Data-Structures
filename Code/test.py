text = "bananas"
pattern = "nas"

starting_index = 0

i = 0
j = 0

# B A N A N A S
# N A S

while i < len(text):
	print(starting_index)
	if text[i] == pattern[j]:
		j += 1
		i += 1
		if j == len(pattern):
			print("mondale")
	else:
		starting_index += 1
		i = starting_index
		j = 0

