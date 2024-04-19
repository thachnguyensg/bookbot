def main() -> int:
    filepath = "books/frankenstein.txt"
    content = read_book(filepath)
    wc = word_count(content)
    print("word count: ", wc)
    lc = letter_count(content)
    print("letter count: ", lc)
    return 0


def read_book(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()


def word_count(content: str) -> int:
    return len(content.split())


def letter_count(content: str) -> dict[str, int]:
    letter_dict: dict[str, int] = {}
    for letter in content:
        lower_letter = letter.lower()
        if lower_letter in letter_dict:
            letter_dict[lower_letter] = letter_dict[lower_letter] + 1
        else:
            letter_dict[lower_letter] = 1

    return letter_dict


main()
