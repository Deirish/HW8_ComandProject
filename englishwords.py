# Вспоминаем работу с файлом. Есть файл, в котором много англоязычных текстовых строк.
# Считаем частоту встретившихся слов в файле, но через функции и map,
# без единого цикла!

from collections import Counter

with open("EnglishText.txt", "r") as file:
 lines = file.read()

# print(Counter([''.join(filter(str.isalpha, x.lower())) for x in lines.split() if ''.join(filter(str.isalpha, x.lower()))]))

def count_word(word):
 if word in total_count:
  total_count[word] += 1
 else:
  total_count[word] = 1


total_count = dict()
list(map(lambda x: count_word(''.join(filter(str.isalpha, x.lower()))), lines.split()))
print(total_count)