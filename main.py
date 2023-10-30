with open("F1.txt", "w") as f1:
    while True:
        line = input("Введите строку (пустая строка для окончания ввода): ")
        if line == "":
            break
        f1.write(line + "\n")

N = int(input("Введите номер строки, с которой начать копирование: "))
K = int(input("Введите номер строки, на которой закончить копирование: "))

with open("F1.txt", "r") as f1, open("F2.txt", "w") as f2:
    lines = f1.readlines()
    for i in range(N-1, K):
        f2.write(lines[i])

vowels = ['a', 'e', 'i', 'o', 'u']
count = 0

with open("F2.txt", "r") as f2:
    text = f2.read()
    for char in text:
        if char.isalpha() and char.lower() not in vowels:
            count += 1

print("Количество согласных букв:", count)

