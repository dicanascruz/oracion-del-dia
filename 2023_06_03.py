import os
import re


def split_bible_quotes(quotes):
    new_quotes = []
    for quote in quotes:
        match = re.search(r'(\d?\s?[a-zA-ZáéíóúÁÉÍÓÚ]+\s\d+:\d+(-\d+)?|\d?\s?[a-zA-ZáéíóúÁÉÍÓÚ]+\s\d+(-\d+)?(:\d+(-\d+)?)?)', quote)
        if match:
            verse_range = match.group(1)
            book_chapter, verses = verse_range.split(':')
            if '-' in verses:
                start_verse, end_verse = map(int, verses.split('-'))
                for verse in range(start_verse, end_verse + 1):
                    new_quote = f"{book_chapter}:{verse}"
                    new_quotes.append(new_quote)
            else:
                new_quotes.append(quote)
        else:
            new_quotes.append(quote)
    return new_quotes


file_path = 'C:\\Users\\Perso\\Desktop\\diego\\Formations Diego\\formation codeur\\python\\projet la priere du jour\\oracion del dia.txt'
output_path = 'C:\\Users\\Perso\\Desktop\\diego\\Formations Diego\\formation codeur\\python\\projet la priere du jour\\resultado.txt'

with open(file_path, 'r') as file:
    content = file.read()

pattern = re.compile(r'\b\d?\s?[a-zA-ZáéíóúÁÉÍÓÚ]+\s\d+:\d+-?\d*\b')

bible_quotes = pattern.findall(content)

bible_quotes = split_bible_quotes(bible_quotes)

print("Las citas bíblicas del día son: ")
for quote in bible_quotes:
    print(quote)

name_list = ["Mariluz", "Ana Mercedes", "Guillermo", "Sofía", "Diego Fernando",
             "Camila", "Pat", "Ana Jael", "Nancy", "Sergio", "Carmen", "Francisco", "Silvia", "José Gregorio"]
assigned_quotes = {}

# Eliminar citas duplicadas
unique_quotes = list(set(bible_quotes))

for i in range(len(name_list)):
    if i < len(unique_quotes):
        assigned_quotes[name_list[i]] = unique_quotes[i]
    else:
        assigned_quotes[name_list[i]] = unique_quotes[i % len(unique_quotes)]

print("\nMuy buenos y santos días hermanos(as), es un honor y un gran placer para mí de servir a nuestra comunidad al compartir las citas del día de hoy:\n")
for name, quote in assigned_quotes.items():
    print(name + ": " + quote)

texto = "Dios los bendiga porque el nombre de Jesús tiene poder para obrar en nuestras vidas hermanos!!!"

with open(output_path, 'w') as outfile:
    outfile.write("Las citas bíblicas del día son: \n")
    for quote in unique_quotes:
        outfile.write(quote + "\n")

    outfile.write("\nMuy buenos y santos días hermanos(as), es un honor y un gran placer para mí de servir a nuestra comunidad al compartir las citas del día de hoy:\n")
    for name, quote in assigned_quotes.items():
        outfile.write(name + ": " + quote + "\n")

    outfile.write("\n" + texto)

with open(output_path, 'r') as f:
    print("\nResultado:\n" + f.read())
