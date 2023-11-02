def solution():
    # Define Sarah's total number of books and number of each type
    sarah_total_books = 6 + 4
    sarah_paperback = 6
    sarah_hardback = 4

    # Calculate the number of paperback and hardback books Sarah's brother bought
    brother_paperback = sarah_paperback / 3
    brother_hardback = sarah_hardback * 2

    # Calculate the total number of books Sarah's brother bought
    brother_total_books = brother_paperback + brother_hardback
    result = brother_total_books
    return result

print(solution())