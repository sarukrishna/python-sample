import string

word_set = set()
sonet_words = open("sonnets.txt").readlines()

def stripped(word):
    appostapi_index = word.find("'")
    if appostapi_index != -1:
        return None
    return word.strip(string.punctuation)


for line in sonet_words:
    word_list = line.replace("-", " ").strip().split()
    if len(word_list) <= 1:
        continue
    for word in word_list:
        stripped_word = stripped(word)
        if stripped_word and len(stripped_word) > 1:
            word_set.add(stripped_word)

word_list = list(word_set)
word_list.sort()

word_file = open("words_sonet.txt", "w")
for sorted_word in word_list:
    word_file.write(sorted_word.upper() + "\n")


    

	