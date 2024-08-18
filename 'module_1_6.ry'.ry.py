phone_book = {'Denis': 89525329109, 'Max': 89156599999}
print( phone_book)
print(phone_book['Denis'])
phone_book['Denis'] = 45
print(phone_book)
del phone_book['Max']
print(phone_book)
phone_book.update({'Sasha': 123 , 'Alex': 456})
print(phone_book)
print(phone_book.get('Denis'))
phone_book.pop('Alex')
print(phone_book)
print(phone_book.keys())
print(phone_book.values())
print(phone_book.items())
set_ = {1, 2, 3, 4, 5, 1, 2, 3, 4, 'String' , True, (1, 2, 3)}
print(set_)
list_ = [1, 1, 1, 1, 2, 2, 3, 2, 2]
print(set(list_))
list_ = set(list_)
print(list_)
print(list_.remove(1))
print(list_)
print(list_.add(5))
print(list_)
my_dict = {"Larisa": 1958, "Sveta": 1954, "Olesya": 1986}
print(my_dict)
print(my_dict["Larisa"])
print(my_dict.get("Ahton", "Такого ключа нет"))
my_dict.update({"Katya" : 2018, "Anatoly" : 1990})
print(my_dict)
my_set = {1, 9, 5, 8, 'Larisa', True, 1, 9, 5}
print(my_set)
my_set.update({17,9})
print(my_set)
my_set.discard(1)
print(my_set)






