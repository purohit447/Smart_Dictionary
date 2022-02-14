# my dictionary app
import json
import time
from difflib import get_close_matches

data = json.load(open("2.2 data.json.json"))


def translate(fn_word):
    search = fn_word.lower()
    if search in data:
        output = data[search]
        for item in output:
            print(' %s'% item)
    elif len(get_close_matches(search, data.keys())) > 0:
        print(' did you mean %s instead?' % get_close_matches(search, data.keys())[0])
        print(' press Y to proceed and N to discontinue.\n')
        choice = input(' ')
        choice = choice.lower()
        if choice == 'y':
            output = data[get_close_matches(search, data.keys())[0]]
            for item in output:
                print(' %s'% item)
        elif choice == 'n':
            print(' Sorry! no word found.')
        else:
            print(" Sorry! We didn't understand your query.")
    else:
        print(' Sorry! no word found.')


print(" hey, I'm here to help you translate words.\n")
choice = 'y'
while choice == 'y':
    word = input(" tell me a word: ")
    translate(word)

    print('\n do you have another word? if yes press Y or ANY key to exit.')
    choice = input(' ')
    choice = choice.lower()
print(" happy to help you.")
time.sleep(2)
