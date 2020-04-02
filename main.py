import argparse


parser = argparse.ArgumentParser(description='write new words')
parser.add_argument('command')


def save_new_words_en_ru(en, ru):
    f = open('dictionary.txt','a')
    f.write('{en}|{ru}\n'.format(en=en, ru=ru))
    return True


def get_all_words_from_dictionary():
    f = open('dictionary.txt','r')
    data = f.read()
    return data.replace('|',' - ')



if __name__== '__main__':
    args = parser.parse_args()
    if 'add' == args.command:
        en_word = input("write a new english word:")
        ru_word = input("write its russian translation:")
        save_new_words_en_ru(en=en_word, ru=ru_word)
        print('new word is added to the dictionary')
    if 'mget' == args.command:
        print(get_all_words_from_dictionary())
