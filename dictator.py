import pickle
from collections import Counter

dictator = dict()
with open("Fraza.txt", "r") as f:
    for line in f:
        val = line
        line = line.replace(" ", "").replace("-", "").replace(",", "").replace("\n", "").lower()
        dictator[val] = Counter(line)

pickle.dump(dictator, open("dictator.pkl", "wb"))
