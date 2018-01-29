from os import listdir
from os.path import isfile, splitext


def get_words(path):
    """get words' list from file with specified name as argument"""
    try:
        with open(path) as obj:
            content = obj.read()
    except FileNotFoundError:
        print('There\'s no such file')
    else:
        words = content.split()
        return words


def get_files(path=None):
    """get list of .txt files in specified directory"""
    try:
        files = [f for f in listdir(path)
                 if isfile(f) and splitext(f)[-1] == '.txt']
    except FileNotFoundError:
        print("There's no such directory...")
        return []
    else:
        return files


# for f in get_files('.'):
#     print('file "' + str(f) + '" : ')
#     print(get_words(f))
#     print()