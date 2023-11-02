def solution():
    sarah_paperbacks = 6
    sarah_hardbacks = 4

    # Calculate the number of paperback books Sarah's brother bought
    brother_paperbacks = sarah_paperbacks / 3

    # Calculate the number of hardback books Sarah's brother bought
    brother_hardbacks = sarah_hardbacks * 2

    # Calculate the total number of books Sarah's brother bought
    total_books = brother_paperbacks + brother_hardbacks
    result = total_books
    return result

print(solution())