def solution():
    # Calculate the total number of members in the book club
    total_members = 3 * 2 + 5 + 2

    # As each member gets to pick a book once in 52 weeks
    # So Ron gets to pick a book once for every (total_members - 1) weeks
    # Also considering that Ron and his wife can pick a book together
    books_per_year = 52 // (total_members - 1)

    result = books_per_year
    return result

print(solution())