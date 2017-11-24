from sample import hello

VOWELS = "aeiou"
def has_any_vowels(word):
    for vowel in VOWELS:
	    if vowel in word:
		    return True

def has_all_vowels(word):
    for vowel in VOWELS:
	    if vowel not in word:
		    return False
    return True

for word in hello.word_list:
    if has_all_vowels(word):
	    print (word) 

    
            		
