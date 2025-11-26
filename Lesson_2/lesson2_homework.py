# 1. Работа с целыми и вещественными числами
a = 2
b = 3
x = 2.1
y = 3.2

print(a)
print(b)
print(x)
print(y)
print(type(a))
print(type(b))
print(type(x))
print(type(y))

# 2. Основные арифметические операции
num1 = 10
num2 = 3
a = num1 +  num2
print(a)
b = num1 - num2
print(b)
c = num1 * num2
print(c)
d = num1 / num2
print(d)
e = num1 // num2
print(e)
f = num1 % num2
print(f)
g = num1 ** num2
print(g)

# 3. Особенности работы с делением
a = 10
b = 3
c = a/b
d = a//b
e = a % b
print(c)
print(d)
print(e)

a = -10
b = 3
c = a/b
d = a//b
e = a % b
print(c)
print(d)
print(e)

a = 10
b = -3
c = a/b
d = a//b
e = a % b
print(c)
print(d)
print(e)

# 4. Работа с приоритетом операторов
a = 5 + 3 * 2
print(a)
b = (5 + 3) * 2
print(b)
c = 10 / 2 ** 2
print(c)

# 5. Использование сокращенных операторов
count = 10
count += 5
count -= 3
count *= 2
count /= 4
print(count)

# "Строки в Python".
# 1. Создание строк

s1 = "Python"
s2 = 'Программирование'
print(s1)
print(s2)
s3 = """
это
многострочная
строка"""
print(s3)

empty = ""
print(len(empty))

# 2. Конкатенация строк
first_name = "Иван"
last_name = "Петров"
full_name = last_name + " " + first_name
print(full_name)

# 3. Преобразование типов
s = "Возраст: "
age = 25
b = s + str(age)
print(b)

# 4. Дублирование строк
a = "ха"
b = a * 5
print(b)
# c = a * 2.5
# print(c)
#Выдает ошибку.

# 5. Длина строки
text = "Привет, мир!"
print(len(text))
text2 = ""
print(len(text2))

# 6. Проверка вхождения подстроки
sentence = "Я изучаю Python"
print("Python" in sentence)
print("Java" in sentence)

# 7. Сравнение строк
a = "apple"
b = "banana"
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
# False
# True
# True
# False
# True
# False

# 8. Код символов
print(ord("А"))
print(ord("а"))
print(ord("я"))
# 1040
# 1072
# 1103