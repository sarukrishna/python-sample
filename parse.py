#Read the txt file and find the links
#open the each link
#read the content inside the link
#write into a new file
#
import re
from nltk import tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def parse(file):
    name = file.split('/')[-1].split('.')[0].strip('tag')
    f = open(file, 'r', encoding='charmap')
    content = f.readlines()
    inputString = "Abraham Lincoln # President of # the United States of America"
    inputSplit = word_tokenize(inputString)
    stop_words = set(stopwords.words('english'))
    filtered_sentense = [w for w in inputSplit if w not in stop_words]
    #all_tags = ['he', 'his', 'him']

    inputQuery = ' '.join(filtered_sentense).split(' # ')
    subjent = inputQuery[0]
    predicate = inputQuery[1]
    objecT = inputQuery[2]

    #inputQuery = ' '.join(inputQuery).split(' ')


    print(inputQuery)
   
    #import pdb;pdb.set_trace()

    for line in content:
        if line.startswith('<') or line.startswith('=='):
            continue
        sentenses = tokenize.sent_tokenize(line)
        for sentense in sentenses:
            if (any(word in sentense for word in inputQuery[0].split(' ')) and 
                any(word in sentense for word in inputQuery[1].split(' ')) and 
                any(word in sentense for word in inputQuery[2].split(' '))):
                if "TIMEX3" in sentense:
                    match = re.findall(r'>(.*?)</TIMEX3>', sentense)
                    if match:
                        print(match)
                        with open("output/" + name + "_filter.txt", "a", encoding='charmap') as f:
                            f.write(str(sentense) + '\n' + str(match))
    f.close()
         

if __name__ == "__main__":
    parse("output/Abraham Lincoln tag.txt")