def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False

    if word[low_index] != word[high_index]:
        return False

    # qd só tem 1 letra
    if low_index >= high_index:
        return True

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)


print(is_palindrome_recursive("", 0, 0))       # False
print(is_palindrome_recursive("arara", 0, 4))  # True
print(is_palindrome_recursive("livia", 0, 4))  # False
print(is_palindrome_recursive("bb", 0, 1))  # True
