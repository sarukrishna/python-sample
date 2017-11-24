from sample import hello
def is_palindrome(word):
    for index in range(len(word)):
        if word[index] != word[-(index+1)]:
	        return False
    return True

longest = ""
for word in hello.word_list:
    if word == word[::-1] and len(word) > len(longest):
	    longest = word
print (longest) 


