first_name = "Sonya"
last_name = "Romanova"
full_name = f"Hello, {first_name} your surname is {last_name}?"
print(full_name)

print(first_name.lower())

print(first_name.upper())

print(first_name.title())

citata = 'Надо любить жизнь больше, чем смысл жизни - "Федор Достоевский"'
print(citata)

autor_name = "Федор Достоевский"
citata2 = f'Надо любить жизнь больше, чем смысл жизни - "{autor_name}"'
print(citata2)

autor_name2 = "\tФедор Достоевский\n"
citata3 = f'Надо любить жизнь больше, чем смысл жизни - "{autor_name2.strip()}"'
print(citata3)
