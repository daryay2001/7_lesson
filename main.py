# Задание 1
#
# В списке целых, заполненном случайными числами вычислить:

# nums = [1, 3, 2, -5, -2, 7, 3, -7, 9, 3]
# print(nums)

# ■ Сумму отрицательных чисел;
# sum1 = 0
# for num in nums:
#     if num < 0:
#         sum1 += num
#
# print(sum1)
#
# # ■ Сумму четных чисел;
# sum2 = 0
# for num in nums:
#     if num % 2 == 0:
#         # print(num)
#         sum2 += num
#
# print(sum2)
#
#
# # ■ Сумму нечетных чисел;
# sum3 = 0
# for num in nums:
#     if num % 2 != 0:
#         sum3 += num
#
# print(sum3)
#
#
# # ■ Произведение элементов с индексами кратными 3;
# mult = 1
# for i in range(len(nums)):
#     if i % 3 == 0:
#         mult *= nums[i]
#
# print(mult)

# ■ Произведение элементов между минимальным и максимальным элементом;
# min_value = min(nums)
# max_value = max(nums)
# min_value_index = nums.index(min_value)
# max_value_index = nums.index(max_value)
# print(min_value_index)
# print(max_value_index)
#
# if max_value_index - min_value_index != 0:
#     if min_value_index > max_value_index:
#         min_value_index, max_value_index = max_value_index, min_value_index
#
#     mult = 1
#
#     for i in range(min_value_index + 1, max_value_index):
#         mult *= nums[i]
#
#     print(mult)


# ■ Сумму элементов, находящихся между первым и последним положительными элементами.
# first_index = 0
# last_index = 0
#
# for i in range(len(nums)):
#     if nums[i] > 0:
#         first_index = i
#         break
#
# for i in range(len(nums) - 1, -1, -1):
#     if nums[i] > 0:
#         last_index = i
#         break
#
# print(first_index)
# print(last_index)
#
# # сделать проверку на наличие чисел между first_index и last_index
# if first_index != last_index:
#     my_sum = 0
#     for i in range(first_index + 1, last_index):
#         my_sum += nums[i]
#
#     print(my_sum)

# Задание 2
#
# Есть список целых, заполненный случайными числами. На основании данных этого массива нужно:
#
# ■ Создать список целых, содержащий только четные числа из первого списка;
# nums1 = []
# for num in nums:
#     if num % 2 == 0:
#         nums1.append(num)
#
# print(nums1)
#
# # ■ Создать список целых, содержащий только нечетные числа из первого списка;
# nums1 = []
# for num in nums:
#     if num % 2 != 0:
#         nums1.append(num)
#
# print(nums1)
#
# # ■ Создать список целых, содержащий только отрицательные числа из первого списка;
# nums1 = []
# for num in nums:
#     if num < 0:
#         nums1.append(num)
#
# print(nums1)
#
# # ■ Создать список целых, содержащий только положительные числа из первого списка.
# nums1 = []
# for num in nums:
#     if num >= 0:
#         nums1.append(num)
#
# print(nums1)

##########
# 1. Пользователь вводит с клавиатуры номер дня недели (1-7).
# Необходимо вывести на экран названия дня недели.
# Например, если 1, то на экране надпись понедельник, 2 — вторник и т.д.
# day_number = int(input("Enter day number: "))
# # v1
# if day_number == 1:
#     print("monday")
# elif day_number == 2:
#     print("tuesday")
# elif day_number == 3:
#     print("wednesday")
# elif day_number == 4:
#     print("thursday")
# elif day_number == 5:
#     print("friday")
# elif day_number == 6:
#     print("saturday")
# elif day_number == 7:
#     print("sunday")
# else:
#     print("Incorrect day number!")
#
# # v2
# match day_number:
#     case 1:
#         print("monday")
#     case 2:
#         print("tuesday")
#     case 3:
#         print("wednesday")
#     case 4:
#         print("thursday")
#     case 5:
#         print("friday")
#     case 6:
#         print("saturday")
#     case 7:
#         print("sunday")
#     case _:
#         print("Incorrect day number!")

# 2. Пользователь вводит два числа.
# Определить, равны ли эти числа, и, если нет, вывести их на экран в порядке возрастания
# n1, n2 = int(input("Enter first number: ")), int(input("Enter second number: "))
# if n1 == n2:
#     print("Equals!")
# elif n1 > n2:
#     print(n2)
#     print(n1)
# else:
#     print(n1)
#     print(n2)

# 3. Пользователь вводит два числа и матем действие: + - * или /
# n1, n2 = int(input("Enter first number: ")), int(input("Enter second number: "))
# math_action = input("Enter math action: + - * /  ")
# match math_action:
#     case "+":
#         print(n1 + n2)
#     case "-":
#         print(n1 - n2)
#     case "*":
#         print(n1 * n2)
#     case "/":
#         if n2 != 0:
#             print(n1 / n2)
#         else:
#             print("Division by zero!")
#     case _:
#         print("Incorrect math action!")

# В зависимости от введенного матем действия вывести результат

################################
####
# def say_hello():
#     print("Hello")
#
#
# # вызовы функции
# say_hello()
# say_hello()
#
#
# def say_hello():
#     print("Hello world")
#
#
# say_hello()
# say_hello()


# def hello_user(name, age): print(f"Hello, {name} your age: {age}")
#
#
# username = "Vasya"
# hello_user(username, 33)
# hello_user("Petya", 44)

##
# def print_messages():
#     # определение локальных функций
#     def say_hello(): print("Hello")
#
#     def say_goodbye(): print("Good Bye")
#
#     # вызов локальных функций
#     say_hello()
#     say_goodbye()
#
#
# # Вызов функции print_messages
# print_messages()

###############
###
# def show_info(surname, name="noname", hobby="no hobby"):
#     print(f"Name: {name} surname: {surname} hobby: {hobby}")
# #
# #
# show_info(name=input("Enter your name: "), surname=input("Enter your surname: "), hobby=input("Enter your hobby: "))
# show_info("Vasya", "Petrov", "qwerty")
# show_info("Vasya", "Petrov")
# show_info(name="Vasya", surname="Ivanov")

############
##
# Символ * позволяет установить, какие параметры будут именнованными - то есть такие параметры,
# которым можно передать значения только по имени. Все параметры,
# которые располагаются справа от символа *, получают значения только по имени:

# def print_person(name, *, age, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person("Bob", age=41, company="Microsoft")
#
# #
# def print_person(*, name, age, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person(name="Bob", age=41, company="Microsoft")

# Если наоборот надо определить параметры, которым можно передавать значения только по позиции,
# то есть позиционные параметры, то можно использовать символ /: все параметры, которые идут до символа / ,
# являются позиционными и могут получать значения только по позиции

# def print_person(name, /, age, company="Microsoft"):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person("Tom", company="JetBrains", age=24)  # Name: Tom  Age: 24  company: JetBrains
# print_person("Bob", 41)

#
# def print_person(name, /, age=18, *, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
# #
# print_person("Sam", company="Google")  # Name: Sam  Age: 18  company: Google
# print_person("Tom", 37, company="JetBrains")  # Name: Tom  Age: 37  company: JetBrains
# print_person("Bob", company="Microsoft", age=42)  # Name: Bob  Age: 42  company: Microsoft

#
# def add(num1, num2):
#     return num1 + num2
# # # return - вернет результат работы функции. После отрабатывания return - все остальные действия функции не отработают
# # # и функция завершит свою работу. return как break, но для функции в отличие от break - вернет результат, а не просто
# # # остановит действия. Если в функции есть циклы, и в одном из циклов сработал return - функция прекратит свою работу.
# # # ключевое слово return может встречаться в теле функции сколько угодно раз
# # #
# # #
# result = add(2, 4)
# print(result)


###
# def add(a, b):
#     return a + b
#
#
# def division(a, b):
#     return a / b


# def calculate():
#     n1 = int(input("Enter first number: "))
#     n2 = int(input("Enter second number: "))
#     math_action = input("Enter math action: + / ")
#     match math_action:
#         case "+":
#             print(f"{n1} {math_action} {n2} = {add(n1, n2)}")
#         case "/":
#             print(f"{n1} {math_action} {n2} = {division(n1, n2)}")
#         case _:
#             raise Exception("Incorrect math action!")
#
#
# try:
#     calculate()
# except ZeroDivisionError:
#     print("Нельзя делить на ноль!")
# except ValueError:
#     print("Введите только цифры!")
# except Exception as error:
#     print(error)

#############
# 2. Даны два списка чисел.
#
# Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.

# nums_1 = [2, 4, 1, 5, 7]
# nums_2 = [5, 2, 8, 6, 1, 4, 9]
# #
# #
# def calc_number_of_equals_numbers_v1(numbers_1, numbers_2):
#     def get_number_of_equals_numbers(first_numbers, second_numbers):
#         counter = 0
#         for number in first_numbers:
#             if number in second_numbers:
#                 counter += 1
#         return counter
#     if len(numbers_1) < len(numbers_2):
#         return get_number_of_equals_numbers(numbers_1, numbers_2)
#     else:
#         return get_number_of_equals_numbers(numbers_2, numbers_1)
#
#
# def calc_number_of_equals_numbers_v2(numbers_1, numbers_2):
#     return len(set(numbers_1).intersection(set(numbers_2)))
#
# #
# result = calc_number_of_equals_numbers_v1(nums_1, nums_2)
# print(result)
# #
# #
# result = calc_number_of_equals_numbers_v2(nums_1, nums_2)
# print(result)

############
#
#  Дан текст: в первой строке записано число строк, далее идут сами строки.
# Определите, сколько различных слов содержится в этом тексте.

# def generate_text(seed="Hello", multiplier=5):
#     return seed * multiplier
#
#
# def calc_diff_strings(text: str) -> int:
#     print(text)
#     print(text.split())
#     return len(set(text.split()))
#
#
# print(calc_diff_strings(generate_text("Hello world", 10)))
# print(calc_diff_strings("Hello how are you thank you"))

# [1, 1, 3, 5]
# [1, 3, 5]
