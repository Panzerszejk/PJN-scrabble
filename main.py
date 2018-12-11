import sys
import time
import pickle
from collections import Counter

global_beg = time.time()
beg = time.time()
letters = sys.argv[1].split()
letter_dict = Counter()
for arg in letters:
    letter_dict[arg] += 1

letter_dict['zero'] = 2
letter_dict_count = sum(letter_dict.values())
letter_point = Counter({'a': 1, 'e': 1, 'i': 1, 'n': 1, 'o': 1, 'r': 1, 's': 1, 'w': 1, 'z': 1,'c':2, 'd':2,'k':2,'l':2,
                        'm':2,'p':2,'t':2,'y':2,'b':3, 'g':3, 'h':3, 'j':3, 'ł':3, 'u':3, 'ą':5, 'ę':5, 'f':5, 'ó':5,
                        'ś':5,'ż':5,'ć':6,'ń':7,'ź':9})


end = time.time()
print("Argumenty pobrano w: ")
print(end - beg)

dictator = pickle.load(open("dictator.pkl","rb")) #dlugo zajmuje

beg = time.time()
victory_line = ''
points = 0

#dictator = dict() #do testowania
#dictator['i to by było na tyle'] = Counter("itobybyłonatyle") #do testowania

for key in dictator:
    temp = dictator[key]
    line_length = sum(temp.values())
    if line_length <= letter_dict_count:
        dict_copy = letter_dict.copy()
        success = True
        points_temp = 0
        blank = 0
        for value_key in temp:
            number_letters = temp[value_key]
            difference = dict_copy[value_key] - number_letters
            if difference >= 0:
                points_temp += letter_point[value_key] * number_letters
            else:
                if difference-blank == -1:
                    blank = -1
                else:
                    success = False
                    break
        if success:
            if points_temp > points:
                points = points_temp
                victory_line = key


end = time.time()
print("Wybor slowa i podliczenie punktow w: ")
print(end - beg)


global_end = time.time()
print("Calosc trwala: ")
print(global_end - global_beg)

print("Wyrażenie: "+victory_line +" Punkty: "+ str(points))



