def get_num_words(file):
    with open(file) as f:
        file_contents = f.read()
        words = file_contents.split()
        return len(words)


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        # print(file_contents)
        return file_contents


def sort_on(items):
    return items["num"]


def count_characters(file):
    with open(file) as f:
        file_contents = f.read()
        words = file_contents.lower()
        counts = {}
        counts_list = []

        # print(words)
        for w in words:
            if w not in counts:
                counts[w] = 0
            counts[w] = counts[w] + 1

        for k, v in counts.items():
            if k.isalpha():
                counts_list.append({"char": k, "num": v})

        counts_list.sort(reverse=True, key=sort_on)
        return counts_list


def print_result(result):
    lines = []
    for item in result:
        lines.append(f"{item['char']}: {item['num']}")
    return "\n".join(lines)
