import random

size = int(input("Enter list length: "))
low_val = int(input("Enter minimum two-digit integer (10..99): "))
high_val = int(input("Enter maximum two-digit integer (10..99): "))

low_val = max(10, min(99, low_val))
high_val = max(10, min(99, high_val))
if low_val > high_val:
    low_val, high_val = high_val, low_val

initial_list = [random.randint(low_val, high_val) for _ in range(size)]
digit_sums = [(abs(num) // 10) + (abs(num) % 10) for num in initial_list]
paired_tuples = [(initial_list[i], digit_sums[i]) for i in range(size)]

print(f"Initial list ({len(initial_list)} items): {initial_list}")
print("Digit sums list: {}".format(digit_sums))
print(f"Paired tuples list: {paired_tuples}")