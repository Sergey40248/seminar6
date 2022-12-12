#  Дан список, вывести отдельно буквы и цифры, пользуясь filter.
# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]
# Все задачи решать с помощью использования 
# лямбд, filter, map, zip, enumerate, 

# a = [12,'sadf',5643]
# stro = list(filter(lambda x: isinstance(x, str),a))

# print(stro,)

a = [12,'sadf',5643]
s = list(filter(lambda x: isinstance(x, str),a))
i = list(filter(lambda x: isinstance(x, int),a))
print(f'{s}, {i}')