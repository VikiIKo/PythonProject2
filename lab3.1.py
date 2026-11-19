start_char = input("Enter starting lowercase Latin letter (or Enter for 'a'): ").strip() or "a"
end_char = input("Enter ending lowercase Latin letter (or Enter for 'z'): ").strip() or "z"

start_code = ord(start_char[0].lower())
end_code = ord(end_char[0].lower())

if start_code > end_code:
    start_code, end_code = end_code, start_code

alphabet_line = "".join(chr(code) for code in range(start_code, end_code + 1))

sequence = input("Enter a sequence of characters: ")

max_run = 0
current_run = 0

for ch in sequence:
    if ch == "a":
        current_run += 1
        if current_run > max_run:
            max_run = current_run
    else:
        current_run = 0

print(f"Generated Latin string ({len(alphabet_line)} chars): {alphabet_line}")
print("Input sequence of length {} chars: {!r}".format(len(sequence), sequence))
print(f"Longest consecutive sequence of 'a': {max_run}")