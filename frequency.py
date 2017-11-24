from matplotlib import pyplot
import string
data = open("constitution.txt", "r").read()
letter_dic = {}
for char in string.ascii_lowercase:
    letter_dic[char] = 0
	
for elt in data:
    if elt in letter_dic:
	    letter_dic[elt] = letter_dic[elt] + 1
	
frequencies = sorted(letter_dic.items())
letters = []
frequency = []

for letter, count in sorted(letter_dic.items()):
    letters.append(letter)
    frequency.append(count)
x_locations = range(len(frequencies))
pyplot.xticks([elt+0.5/2 for elt in x_locations], letters)
pyplot.bar(x_locations, frequency, width=0.5)
pyplot.show()