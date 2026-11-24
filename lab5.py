def build_dictionary_book(dictionary_data: dict[str, tuple[str, ...]]) -> str:
    lines = ["=== DICTIONARY BOOK ==="]

    for letter, words in dictionary_data.items():
        formatted_words = ", ".join(words) if words else "— (no words)"
        line = "Letter [{0}] ({1}): {2}".format(
            letter.upper(),
            len(words),
            formatted_words,
        )
        lines.append(line)

    return "\n".join(lines)


def main() -> None:
    alphabet_dict: dict[str, tuple[str, ...]] = {}

    raw_input_data = input(
        "Enter a dictionary in the format 'A: word1, word2; B: word3, word4': "
    ).strip()

    if raw_input_data:
        entries = raw_input_data.split(";")
        for entry in entries:
            if ":" not in entry:
                continue
            letter_part, words_part = entry.split(":", 1)
            letter = letter_part.strip().upper()
            if not letter:
                continue

            words = tuple(
                word.strip() for word in words_part.split(",") if word.strip()
            )
            alphabet_dict[letter] = words
    else:
        alphabet_dict = {
            "А": ("алгоритм", "аналіз", "архітектура"),
            "Б": ("база", "бібліотека", "блок"),
            "В": ("вузол", "вибірка"),
            "Г": ("графік", "гілка"),
            "Д": ("дані", "дерево", "документація"),
        }

    output = build_dictionary_book(alphabet_dict)
    print("\n" + output)


if __name__ == "__main__":
    main()