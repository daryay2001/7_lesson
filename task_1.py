# Задание 1
#
# Напишите функцию, вычисляющую произведение элементов списка целых.
# Список передаётся в качестве параметра. Полученный результат возвращается из функции.
#
# Я так поняла, что список изначально состоит из целых чисел и проверку делать не надо.
# def mult_nums(list_1):
#     mult = 1
#     for i in list_1:
#         mult *= i
#     return print(f"Result = {mult}")
#
# try:
#
#     my_list = [5, 7, 9, 12, 23]
#     mult_nums(my_list)
#
#     second_list = [1, 2, 5]
#     mult_nums(second_list)
#
# except ValueError as error:
#     print(error)
# except Exception as error:
#     print(error)

#
# Задание 2
#
# Напишите функцию для нахождения минимума в списке целых.
# Список передаётся в качестве параметра. Полученный результат возвращается из функции.
#
# def min_list(user_list):
#     return print(f" Min from the list {(min(user_list))}")
#
# try:
#     my_list = [-5, 0, 8, 9]
#     min_list(my_list)
#
#     another_list = [-2, -222, 0, 12]
#     min_list(another_list)
#
# except ValueError as error:
#     print(error)
# except Exception as error:
#     print(error)

#
# Задание 3
#
# Напишите функцию, определяющую количество простых чисел в списке целых.
# Список передаётся в качестве параметра. Полученный результат возвращается из функции.
#
# Простое число — это натуральное число больше 1, у которого есть всего два делителя:
# единица и само число.

# def find_prime_numbers_v1(user_list):
#     def is_prime_v1(number):
#         if number < 2:
#             return False
#         for i in range(2, number): # Перебирает все числа, но можно оптимизировать
#             if number % i == 0:
#                  return False
#         return True
#     count = 0
#     user_list_2 = []
#     for i in user_list:
#         if is_prime_v1(i):
#             user_list_2.append(i)
#             count += 1
#
#
#     return print(f"{user_list_2} \n There are {count} numbers")
#
# try:
#     number_list = [2, 13, 8, 9, 23, 18]
#     find_prime_numbers_v1(number_list)
# except ZeroDivisionError as error:
#     print(error)
# except ValueError as error:
#     print(error)
# except Exception as error:
#     print(error)

####### Version 2

# def find_prime_numbers_v2(user_list):
#     def is_prime_v2(number):
#         if number < 2:
#             return False
# # Т.к. самый большой делитель не может быть больше половины числа, то таким образом сокращаем количество чисел
#         for i in range(2, number // 2 + 1):
#             if number % i == 0:
#                 return False
#         return True
#     count = 0
#     user_list_2 = []
#     for i in user_list:
#         if is_prime_v2(i):
#             user_list_2.append(i)
#             count += 1
#     return print(f"{user_list_2} \n There are {count} numbers")
#
# try:
#     number_list = [2, 13, 8, 9, 23, 18]
#     find_prime_numbers_v2(number_list)
# except ZeroDivisionError as error:
#     print(error)
# except ValueError as error:
#     print(error)
# except Exception as error:
#     print(error)

#
# Задание 4
#
# Напишите функцию, удаляющую из списка целых некоторое заданное число.
# Из функции нужно вернуть количество удаленных элементов.

# def find_del_v1(user_list, *, num): # Т.е. параметр num теперь именованный
#     amount = 0
#     if isinstance(num, int): # Проверяем, что num у нас целое число
#         for i in user_list:
#             if i == num:
#                 user_list.remove(i)
#                 amount += 1
#         return print(f"New list: {user_list} \n Was deleted {amount} elements")
#     else:
#         raise ValueError("Please, enter int")
#
#
# def find_del_v2(user_list, *, num):
#     list_2 = []
#     if isinstance(num, int):
#         amount = user_list.count(num)
#         for i in user_list:
#             if i != num:
#                 list_2.append(i)
#         return print(f"New list: {list_2} \n Was deleted {amount} elements")
#
#     else:
#         raise ValueError("Please, enter int")
#
#
#
# try:
#     my_list = [12, 5, 28, -9, 6, 7, 5, 2, 5]
#     find_del_v1(my_list, num=5)
#     # find_del_v2(my_list, num=5)
#     # find_del_v2(my_list, num="I`m a string")
#
# except ValueError as error:
#     print(error)
# except Exception as error:
#     print(error)

#
#
#
# Задание 5
#
# Напишите функцию, которая получает два списка в качестве параметра
# и возвращает список, содержащий элементы обоих списков.
#
# def add_lists(list_1, list_2):
#     list_3 = list_1 + list_2
#     return print(list_3)
#
#
# try:
#     first_list = [2, 5, 7, 9]
#     second_list = [12, 28, 3, 27, 0]
#     add_lists(first_list, second_list)
#
# except ValueError as error:
#     print(error)
# except Exception as error:
#     print(error)
# #
#
# Задание 6
#
# Напишите функцию, высчитывающую степень каждого элемента списка целых.
# Значение для степени передаётся в качестве параметра, список тоже передаётся в качестве параметра.
# Функция возвращает новый список, содержащий полученные результаты.

# def raise_degree(user_list, *, deg): # Т.е. параметр deg теперь именованный
#     if isinstance(deg, int): # Проверяем, что степень у нас целое число
#         for i in range(len(user_list)):
#             user_list[i] = user_list[i] ** deg
#         return print(f"New list: {user_list}")
#     else:
#         raise ValueError("Please enter int")
#
#
# try:
#     my_list = [5, 7, 2, 1, 10]
#     raise_degree(my_list, deg=3)
#
#     raise_degree(my_list, deg="I`m a string")
#
# except ValueError as error:
#     print(error)
# except Exception as error:
#     print(error)