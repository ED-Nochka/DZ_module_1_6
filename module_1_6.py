# Словари
my_dict = {'Elena': 2010, 'Katya': 2011, 'Mahsa': 2013}
print(my_dict)
print(my_dict['Katya'])
my_dict['Den'] = 2014
print(my_dict)
my_dict.update({'Valera': 2015, 'Liza': 2016})
print(my_dict)
x = my_dict.pop('Mahsa')
print(x)
print(my_dict)
# Множества
my_set = {2, 2.5, 'a', 'b', 2.5, 'a'}
print(my_set)
my_set = {2, 2.5, 'a', 'b', 2.5, 'a', 3.5, 1}
print(my_set)
print(my_set.discard(1))
print(my_set)
