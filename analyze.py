import json
from collections import Counter

def get_filename():

    user_file = input("Enter full path to the json dump: ")
    
    return user_file

filename = get_filename()
messages = []
message_strings = ' '

with open(filename) as f:
    contents = json.load(f)

for i in contents['messages']:
    messages.append((i['text']))
message_strings = ' '.join([str(i) for i in messages])

def get_messages_ammount():
    
    for i in contents['messages']:
        messages.append((i['text']))
    print(f"There are {len(messages)} messages.")

def get_all_messages_length():

    print(f'The length of all messages is: {len(message_strings)}')

def get_top_50_words():
    most_occur = list(Counter(map(str.lower ,message_strings.split())).most_common(50))
    print(f'Top 50 most common words:\n\n{most_occur}')

def get_word_count(word=input("Enter word which you want to count from messages: ")):
    
    ammount = message_strings.strip().lower().count(str(word.lower()))
    if ammount == 1:
        print(f"Word {word} was used: {ammount} time.")
    else:
        print(f"Word {word} was used: {ammount} times.")

get_messages_ammount()
get_all_messages_length()
get_word_count()
get_top_50_words()
