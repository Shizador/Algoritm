# -*- coding: cp1251 -*-
year = int(input("Введите год: "))

if year % 400 == 0 or year % 4 == 0 :
    print("YES")
elif (year % 100 == 0):
    print("NO")
else:
    print("NO")

#2
def print_penguin():
    penguin = [
    "       _~_" ,
    "     ( o o )",
    "    /   V   \ ",
    "   / (  _  ) \ ",
    "      ^^ ^^"
    ]
    return penguin

n = int(input("Введите число от 1 до 9: "))

if 1 <= n <= 9:
    penguin_lines = print_penguin()
    
    for line in penguin_lines:
        print((line + " ") * n)
else:
    print("Введите число от 1 до 9.")

#3
ostring = input("Введите строку: ")

nstring = ""
for char in ostring:
    nstring += char + "*"


if nstring:
    nstring = nstring[:-1]

print("Результат:", nstring)

#4
import re

ip_address = input("Введите IP-адрес: ")

pattern = r'^((25[0-5]|(2[0-4][0-9])|([01]?[0-9][0-9]?))\.){3}(25[0-5]|(2[0-4][0-9])|([01]?[0-9][0-9]?))$'

if re.match(pattern, ip_address):
    print("YES")
else:
    print("NO")

#5
import re

def is_palindrome(s):   
    cleaned = re.sub(r'[^a-zA-Zа-яА-Я0-9]', '', s.lower())
    
    return cleaned == cleaned[::-1]

phrase = input("Введите фразу: ")

if is_palindrome(phrase):
    print("YES")
else:
    print("NO")