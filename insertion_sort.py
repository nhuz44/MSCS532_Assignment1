
def insertion_sort_descending(numbers):
    """
    Sort a list of numbers in monotonically decreasing order
    using the Insertion Sort algorithm.
    """
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1

        # Move smaller elements one position to the right.
        while j >= 0 and numbers[j] < key:
            numbers[j + 1] = numbers[j]
            j -= 1

        # Insert the key in its correct position.
        numbers[j + 1] = key

    return numbers


if __name__ == "__main__":
    numbers = [12, 5, 9, 2, 18, 7]

    print("Original array:", numbers)

    insertion_sort_descending(numbers)

    print("Sorted array (descending):", numbers)
