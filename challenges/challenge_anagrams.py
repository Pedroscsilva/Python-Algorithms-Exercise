def is_anagram(first_string, second_string):
    first_list = list(first_string.lower())
    second_list = list(second_string.lower())

    quick_sort(first_list, 0, len(first_list) - 1)
    quick_sort(second_list, 0, len(second_list) - 1)

    first_string = "".join(first_list)
    second_string = "".join(second_list)

    if first_string == "" or second_string == "":
        return_bool = False
    else:
        return_bool = first_string == second_string

    return (first_string, second_string, return_bool)


def quick_sort(letters, start, end):
    if start < end:
        p = partition(letters, start, end)
        quick_sort(letters, start, p - 1)
        quick_sort(letters, p + 1, end)


def partition(letters, start, end):
    pivot = letters[end]
    delimiter = start - 1

    for i in range(start, end):
        if letters[i] <= pivot:
            delimiter += 1
            letters[i], letters[delimiter] = letters[delimiter], letters[i]

    letters[delimiter + 1], letters[end] = letters[end], letters[delimiter + 1]

    return delimiter + 1
