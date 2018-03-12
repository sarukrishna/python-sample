#Read the txt file and find the links
#open the each link
#read the content inside the link
#write into a new file
#
from nltk import tokenize

def parse(file):
    name = file.split('/')[-1].split('.')[0].strip('tag')
    ignore_tags = ['(', ')', '=', '-', '>', '<']
    f = open(file, 'r', encoding='charmap')
    content = f.readlines()
    all_tags = ['he', 'his', 'him']
    all_tags.append(name)
    words = content[3].strip().split(' ')
    for word in words:
        if any(tag in word for tag in ignore_tags):
            continue
        else:
            all_tags.append(word)
    print(all_tags)
    for line in content:
        if line.startswith('<') or line.startswith('=='):
            continue
        sentenses = tokenize.sent_tokenize(line)
        for sentense in sentenses:
            if any(tag in sentense.lower() for tag in all_tags):
                with open("output/" + name + "_filter.txt", "a", encoding='charmap') as f:
                    f.write(sentense + '\n')
    f.close()
     				

if __name__ == "__main__":
    parse("output/Barack Obama tag.txt")
