BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    text = text[start:]
    rule: list = __import__('string').punctuation
    if len(text) <= size:
        return text, len(text)

    for i in range(size):
        if text[size - i - 1] in rule and text[size - i] not in rule:
            return text[:size - i], size - i


def prepare_book(path: str) -> None:
    count_page: int = 1
    start_next_line: int = 0
    with open(path, encoding='utf-8') as book_file:
        READER: str = book_file.read()
        while True:
            part_text, size_page = _get_part_text(READER, start_next_line, PAGE_SIZE)
            if not part_text:
                break
            book[count_page] = part_text.lstrip()
            count_page += 1
            start_next_line += size_page


prepare_book(BOOK_PATH)
