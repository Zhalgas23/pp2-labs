#1
n = int(input("Number1: "))
squares = (i ** 2 for i in range(1, n + 1))
for square in squares:
    print(square)


#2

n = int(input("Number2: "))
even_numbers = ",".join(str(i) for i in range(0, n + 1, 2))
print(even_numbers)


#3
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Number3: "))
for num in divisible_by_3_and_4(n):
    print(num)


#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input("Number4.1: "))
b = int(input("Number4.2: "))

for square in squares(a, b):
    print(square)


#5
n = int(input("Number5: "))
countdown = (i for i in range(n, -1, -1))

for num in countdown:
    print(num)
