import random

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns (n): "))
min_num = int(input("Enter minimum integer value: "))
max_num = int(input("Enter maximum integer value: "))

if min_num > max_num:
    min_num, max_num = max_num, min_num

matrix = [
    [random.randint(min_num, max_num) for _ in range(cols)]
    for _ in range(rows)
]

even_count = 0
odd_count = 0

for row in matrix:
    for value in row:
        if value % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

print(f"Matrix A ({rows}x{cols}):")
for row in matrix:
    print("  " + " ".join(f"{val:4d}" for val in row))

print("Even count: {} | Odd count: {}".format(even_count, odd_count))