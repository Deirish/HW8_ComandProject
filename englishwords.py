# Вспоминаем работу с файлом. Есть файл, в котором много англоязычных текстовых строк.
# Считаем частоту встретившихся слов в файле, но через функции и map,
# без единого цикла!

from collections import Counter

with open("EnglishText.txt", "r") as file:
 lines = file.read()
word_list = []

for word in lines.split():
    clear_word = " "
    for letter in word:
        if letter.isalpha():
            clear_word += letter.lower()
    word_list.append(clear_word)
print(Counter(word_list))

