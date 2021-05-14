import sys

if len(sys.argv) != 2:
    sys.exit(0)

search_word = input('Search word: ')
file = open(sys.argv[1], 'r')
for lines in file:
    index = lines.find(search_word)
    if index != -1:
        print(index)