import sys
from operator import itemgetter
from os import write

sys.path.append("..")
from reading_files import get_words, get_files
sys.path.pop()

def get_clean_list(old_list):
    for idx, word in enumerate(old_list):
        word = str(word)
        upd_w = word.lower()
        upd_w = upd_w.strip(' .,!?:;"-«()[]\'')
        old_list[idx] = upd_w
    return old_list


files = get_files(path='.')
print(files)
list_of_dict = []
for f in files:
    d = {}
    list_of_words = get_words(f)
    list_of_words = get_clean_list(list_of_words)
    total_amount_of_words = len(list_of_words)
    set_of_words = set(list_of_words)
    cnt = 0
    for i in set_of_words:
        amount = list_of_words.count(i)
        cnt += amount
        d[i] = amount
        print(str(cnt) + " / " + str(total_amount_of_words))
    list_of_dict.append(d)
    out1 = open("output_" + f, 'w')
    out1.write("total amount of words = " + str(total_amount_of_words) + "\n")
    out2 = open("output_more_3_letters_" + f, 'w')
    reduced_amount_of_words = 0
    for key, value in sorted(d.items(), key=itemgetter(1), reverse=True):
        out1.write(str(key))
        if len(key) > 3:
            out2.write(str(key))
            whitesp = 40 - len(key)
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

d = {}
total = 0
maxlen = 0
for dictionary in list_of_dict:
    for key, value in sorted(dictionary.items(), key=itemgetter(1), reverse=True):
        d[key] += value
        total += value

for key, value in sorted(d.items(), key=itemgetter(1), reverse=True):
    if len(key) > maxlen:
        maxlen = len(key)
        maxword = key
        freq = value

out = open('total_stat.txt', 'w')
out.write('Total amount of words = ' + str(total) + "\n")
out.write('The longest word - "' + str(maxword) +
          '"! It\'s frequency = ' + str(freq) + '\n')
out.write('-'*44)
for key, value in sorted(d.items(), key=itemgetter(1), reverse=True):
    out.write(str(key))
    whitesp = 40 - len(key)
    out.write(' ' * whitesp)
    out.write(str(value))
    out.write('\n')
out.close()

# dic = {}
# list_of_word = []
# files = get_files()
# for f in files:
#     all_words = get_words(f)
#
#     # set with uniq values
#     words = set(all_words)
#     for w in words:
#         if w in dict:
#            continue
#         else:
#
