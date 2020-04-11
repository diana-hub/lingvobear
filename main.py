import argparse


parser = argparse.ArgumentParser(description='write new words')
parser.add_argument('command')
file_dictionary = 'dictionary.txt'


def get_last_id():
    f = open(file_dictionary, 'r')
    data = f.read()
    if not data:
        return 0
    # last_string = [i for i in data.split('\n') if i][-1]
    list_str = data.split('\n')
    list_res = []
    for i in list_str:
        if i:
            list_res.append(i)
    last_string = list_res[-1]
    id = last_string.split('|')[0]
    return int(id)


def save_new_words_en_ru(en, ru):
    id = get_last_id() + 1
    f = open(file_dictionary,'a')
    f.write('{id}|{en}|{ru}\n'.format(id=id, en=en, ru=ru))
    return True


def get_all_words_from_dictionary():
    f = open(file_dictionary,'r')
    data = f.read()
    return data.replace('|',' - ')


def get_last_10_words():
    f = open(file_dictionary,'r')
    data = f.read()
    #res = data.split('\n')
    res = [i for i in data.split('\n') if i][-10:]
    return '\n'.join(res).replace('|',' - ')


if __name__== '__main__':
    args = parser.parse_args()
    if 'add' == args.command:
        en_word = input("write a new english word:")
        ru_word = input("write its russian translation:")
        save_new_words_en_ru(en=en_word, ru=ru_word)
        print('new word is added to the dictionary')
    if 'mget' == args.command:
        print(get_all_words_from_dictionary())
    if 'last10' == args.command:
        print(get_last_10_words())
