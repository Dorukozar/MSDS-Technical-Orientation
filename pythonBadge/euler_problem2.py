total = 0

first = 1
second = 2

next1 = first + second

total += second

while next1 < 4000000:

    first = second

    second = next1

    next1 = second + first

    if next1 % 2 == 0:
        total += next1

print(total)