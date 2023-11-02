def solution():
    starting_age = 6
    pages_first_books = 8
    age_double_pages = starting_age * 2
    pages_double_age = pages_first_books * 5
    age_triple_pages = age_double_pages + 8
    pages_triple_age = pages_double_age * 3

    # Calculate the current age and current pages of the books Mandy reads
    current_age = age_triple_pages + 8
    current_pages = pages_triple_age * 4
    result = current_pages
    return result

print(solution())