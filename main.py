def main() -> int:
    book = "books/frankenstein.txt"
    content = read_book(book)
    wc = word_count(content)
    lc = letter_count(content)
    print_report(book, wc, lc)
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


def to_list_letter_dict(letter_count: dict[str, int]):
    list_dict = []
    for k, v in letter_count.items():
        if k.isalpha():
            list_dict.append({"letter": k, "count": v})
    return list_dict


def sort_on(dict):
    return dict["count"]


def print_report(book: str, word_count: int, letter_count: dict[str, int]) -> None:
    print(f"--- Begin report of {book} ---")
    print(f"{word_count} words found in the document")

    list_letter_count = to_list_letter_dict(letter_count)
    list_letter_count.sort(key=sort_on, reverse=True)
    for lc in list_letter_count:
        print(f"The '{lc["letter"]}' character was found {lc["count"]} times")

    print("--- End report ---")


main()
