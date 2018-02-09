import sys
from operator import itemgetter
from os import write

# it's need to get access to top-directory files
sys.path.append("..")
from reading_files import get_words, get_files
sys.path.pop()


def get_clean_list(old_list):
    '''
    The function removes all redudant characters from word to get the
    'clean' word

    :param old_list: list of 'dirty' words
    :return: list of 'clean' words
    '''
    for idx, word in enumerate(old_list):
        word = str(word)
        upd_w = word.lower()
        upd_w = upd_w.strip(' .,!?:;"-«()[]\'')
        old_list[idx] = upd_w
    return old_list


# get all files to process
path_to_files_to_read = '.'
files = get_files(path=path_to_files_to_read)
print(files)

for f in files:
    d = {}
    list_of_words = get_clean_list(get_words(f))
    total_amount_of_words = len(list_of_words)
    cnt = 0
    for i in list_of_words:
        cnt += 1
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
        # some online log
        print(str(cnt) + " / " + str(total_amount_of_words))

    # write statistics to certain file
    out1 = open("output_" + f, 'w')
    out1.write("total amount of words = " + str(total_amount_of_words) + "\n")
    out2 = open("output_more_3_letters_" + f, 'w')
    reduced_amount_of_words = 0
    for key, value in sorted(d.items(), key=itemgetter(1), reverse=True):
        out1.write(str(key))
        if len(key) > 3:
            out2.write(str(key))
            whitesp = 40 - len(key)  # pretty-nice output
            out2.write(' ' * whitesp)
            out2.write(str(value))
            out2.write('\n')
            reduced_amount_of_words += value
        whitesp = 40-len(key)
        out1.write(' ' * whitesp)
        out1.write(str(value))
        out1.write('\n')
    out2.write(str(reduced_amount_of_words))
    out2.close()
    out1.close()