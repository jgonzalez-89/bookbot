# main.py
import sys
from stats import get_num_words, count_characters, print_result


def main(book_path: str):
    # calcula todo usando SOLO el argumento
    word_count = get_num_words(book_path)
    char_count = count_characters(book_path)

    print(f"""
============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
{print_result(char_count)}
============= END ===============
""")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])  # aquí solo pasas el argumento de consola
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)