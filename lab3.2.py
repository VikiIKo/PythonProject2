raw_start = input("Enter starting lowercase Latin letter (Enter for a): ").encode("ascii", errors="ignore")
raw_end = input("Enter ending lowercase Latin letter (Enter for z): ").encode("ascii", errors="ignore")

start_byte = raw_start[:1].lower()[0] if raw_start[:1] else 97
end_byte = raw_end[:1].lower()[0] if raw_end[:1] else 122

if start_byte > end_byte:
    start_byte, end_byte = end_byte, start_byte

alphabet_buf = bytearray()
current_byte = start_byte
while current_byte <= end_byte:
    alphabet_buf.append(current_byte)
    current_byte += 1

alphabet_bytes = bytes(alphabet_buf)

input_bytes = input("Enter a sequence of characters: ").encode("utf-8")
work_buf = bytearray(input_bytes)

target_byte = ord(b"a")
max_streak = 0
current_streak = 0

idx = 0
while idx < len(work_buf):
    if work_buf[idx] == target_byte:
        current_streak += 1
        if current_streak > max_streak:
            max_streak = current_streak
    else:
        current_streak = 0
    idx += 1

result_bytes = bytes(work_buf)

print(f"Alphabet (bytes): {alphabet_bytes!r} | length: {len(alphabet_bytes)} bytes")
print("Input data (bytes): {!r} | size: {} bytes".format(result_bytes, len(result_bytes)))
print(f"Longest consecutive sequence of b'a': {max_streak}")