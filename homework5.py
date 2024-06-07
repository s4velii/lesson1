# food = ['apple', 'coconut', 'banana']
# print(food[0])
# food.append(True)
# print(food)
# food.extend('fruit')
# print(food)
# food.extend(['fruit', 3])
# print(food)
# food.remove('coconut')
# print(food)
# print('coconut' in food)
# print(food[0::2])

# tuple_ = (1, 2, 3, 4)
# print(tuple_)
# kortej = tuple([1, 2, 3, 4])
# print(type(kortej))
# print(tuple_[1])


immutable_var = 10, 'string', 15.5
print('Immutable tuple:', immutable_var)
# immutable_var[0] = 4 ---- TypeError: 'tuple' object does not support item assignment
mutable_list = [10, 'string', 15.5]
print('Mutable_list:', mutable_list)
mutable_list[0] = 99999999
print('Mutable 10 to 99999999:', mutable_list)
mutable_list.append('Modified')
print('Mutable_list_append:', mutable_list)
mutable_list.remove('string')
print('Mutable_list_remove_string', mutable_list)
print('Успешный успех')
