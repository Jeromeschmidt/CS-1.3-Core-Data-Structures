import sys
# from permutation import permutation
from search import binary_search
from itertools import permutations

#### Words must be in mac built in dictionary
#### final jumble must be one word

def get_words():
    words =list(open("/usr/share/dict/words","r"))
    for i in range(len(words)):
        words[i] = words[i].strip()
    return words

def find_answer(words, string):
    result = list()
    perms = permutations(list(string))
    for elm in list(perms):
        # if binary_search(words, ''.join(elm)):
        if ''.join(elm) in words:
            if ''.join(elm) not in result:
                result.append(''.join(elm))
    return result

if __name__ == '__main__':
    words = get_words()
    print("glitz" in words)
    word_list = list()
    word_list.append(str(sys.argv[1]))
    word_list.append(str(sys.argv[2]))
    word_list.append(str(sys.argv[3]))
    word_list.append(str(sys.argv[4]))
    for i in range(len(word_list)):
        word_list[i] = find_answer(words, word_list[i])
    letters = [None] * len(word_list)
    for i in range(len(word_list)):
        letters[i] = list(input("What letters from " + str(word_list[i]) + ": "))
    new_letters = ""
    for i in range(len(letters)):
        for elm in letters[i]:
            new_letters += str(word_list[i][0][int(elm)-1])
    print("Final Jumble: " + str(find_answer(words, str(''.join(new_letters)))))
