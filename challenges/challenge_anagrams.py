
def partition(word, start, end):
    pivot = word[end]
    delimiter = start - 1

    for index in range(start, end):
        if word[index] <= pivot:
            delimiter += 1
            word[delimiter], word[index] = word[index], word[delimiter]
    word[delimiter + 1], word[end] = word[end], word[delimiter + 1]
    return delimiter + 1


def quick_sort(word, start, end):
    if start < end:
        p = partition(word, start, end)
        quick_sort(word, start, p - 1)
        quick_sort(word, p + 1, end)


def word_ordanation(word):
    lowerCase_word = word.lower()
    letters_list = list(lowerCase_word)
    quick_sort(letters_list, 0, len(letters_list) - 1)
    return ''.join(letters_list)


def is_anagram(first_string, second_string):
    sorted_first = word_ordanation(first_string)
    sorted_second = word_ordanation(second_string)

    if not first_string or not second_string:
        return (sorted_first, sorted_second, False)

    return (sorted_first, sorted_second, sorted_first == sorted_second)


print(is_anagram("amor", "roma"))    # ('amor', 'amor', True)
print(is_anagram("pedra", "perda"))  # ('adepr', 'adepr', True)
print(is_anagram("pato", "tapo"))    # ('aopt', 'aopt', True)
print(is_anagram("Amor", "Roma"))    # ('amor', 'amor', True)
print(is_anagram("", ""))            # ('', '', True)
