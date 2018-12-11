import sys
import time
from collections import Counter

global_beg = time.time()
beg = time.time()
letter_dict = Counter()
letters = sys.argv[1].split()
for arg in letters:
    letter_dict[arg] += 1

letter_dict['zero'] = 2
letter_dict_count = sum(letter_dict.values())
letter_point = Counter({'a': 9, 'e': 7, 'i': 8, 'n': 5, 'o': 6, 'r': 4, 's': 4, 'w': 4, 'z': 5, })


end = time.time()
print("Argumenty pobranow w: ")
print(end - beg)

f = open("Frazy.txt", 'r')

beg = time.time()
victory_line = ''
for line in f:
    line_copy = line.replace(" ", "").replace("\n", "").replace(",", "")

    # print("LINIA: "+line_copy+"  "+str(len(line_copy))+" "+str(letter_dict_count))
    if len(line_copy) < letter_dict_count:
        dict_copy = letter_dict.copy()
        success = True
        for letter in line_copy:
            if dict_copy[letter] > 0:
                dict_copy[letter] -= 1
            else:
                if dict_copy['zero'] > 0:
                    dict_copy['zero'] -= 1
                else:
                    success = False
                    #print("fail "+line)
                    break
        if success:
            print(line)

            victory_line = line



end = time.time()
print("Plik przeczytano w: ")
print(end - beg)


global_end = time.time()
print("Calosc trwala: ")
print(global_end - global_beg)

# beg = time.time()
# end = time.time()
# print(end - beg)
#letter_point = Counter({'a': 9, 'e': 7, 'i': 8, 'n': 5, 'o': 6, 'r': 4, 's': 4, 'w': 4, 'z': 5})



