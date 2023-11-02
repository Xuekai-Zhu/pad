def solution():
    adult_books = 104
    percent_children = 0.35

    # Calculate the total number of adult books and children's books
    total_books = adult_books / (1 - percent_children)

    result = total_books
    return result

print(solution())