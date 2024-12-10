# Метод append() упрощает динамическое построение списков.
# Например, вы можете начать с пустого списка и добавлять в него элементы серией команд append().
countries = ['Russia','Germany','Ukraine','Sweden']
print(countries)
countries.append('South Korea')
print(countries)
countries.append('Japan')
countries.append('Turkey')
print(countries)

cities = []
cities.append('Москва')
cities.append('Нижний Новгород')
cities.append('Санкт-Петербург')
cities.append('Уфа')
print(cities)

#Метод insert() позволяет добавить новый элемент в произвольную позицию списка.
# Для этого следует указать индекс и значение нового элемента.

floors = ['second', 'third']
print(floors)
floors.insert(0,'first')
print(floors)

#Если вам известна позиция элемента, который должен быть удален из списка, воспользуйтесь командой del.
print(cities)
del cities[3]
print(cities)

# Метод pop() удаляет последний элемент из списка, но позволяет работать с ним после удаления.

print(countries)
popped_counries = countries.pop()
print(countries)
print(popped_counries)

# команда pop() может использоваться для вывода сообщения о последнем купленном мотоцикле:
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.") #вывод информации о последнем приобретенном мотоцикле
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.") #вывод информации о первом приобретенном мотоцикле
print(motorcycles)

# Иногда позиция удаляемого элемента неизвестна. Если вы знаете только значение элемента, используйте метод remove().
