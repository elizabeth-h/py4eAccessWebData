import re

hand = open('regex_sum_194541.txt')
sum = 0
for line in hand:
    line = line.rstrip()
    text_numbers = re.findall('[0-9]+', line)
    for number in text_numbers:
        sum = sum + float(number)
print(sum)