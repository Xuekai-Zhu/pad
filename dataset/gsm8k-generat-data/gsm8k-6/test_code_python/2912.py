def solution():
    # Calculate the number of books in the third level
    third_level = 64 / 0.8  # each level has 80% as many books as the previous level
    # Calculate the number of books in the second level
    second_level = third_level / 0.8
    # Calculate the number of books in the first level
    first_level = second_level / 0.8
    # Calculate the total number of books in the pyramid
    total_books = 64 + third_level + second_level + first_level
    result = total_books
    return result

print(solution())