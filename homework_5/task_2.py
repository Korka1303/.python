# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.
import codecs

with codecs.open('text.txt', encoding="UTF-8") as file:
    file_lini1 = file.readlines()
    for num, line in enumerate(file_lini1):
        word_count = len(line.split())
        print(f'№{num + 1} - {word_count} слов(о/а)')