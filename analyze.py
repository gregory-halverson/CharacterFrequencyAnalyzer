__author__ = 'Gregory'

import sys

with open(sys.argv[1]) as file:
    text = file.read()

counts = {}

for character in text:
    if not character in counts:
        counts[character] = 1
    else:
        counts[character] += 1

sort = sorted(counts, key = counts.__getitem__, reverse = True)

sort = [elem for elem in sort if elem.isalnum()]

total = 0
for character in sort:
    total += counts[character]

print('character: count, frequency')

for character in sort:
    print(character + ': ' + str(counts[character]) + ', ' + "{0:.2f}%".format(counts[character] / total * 100))


#for character in counts:
#    print(str(character) + ': ' + str(counts[character]))
