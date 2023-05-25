def is_palindrome_iterative(word):
    if word == "":
        return False
    for i, j in zip(range(0, len(word) - 1), range(len(word) - 1, 0, -1)):
        if word[i] != word[j]:
            return False
    return True
