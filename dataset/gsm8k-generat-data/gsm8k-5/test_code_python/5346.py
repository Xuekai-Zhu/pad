def solution():
    # Calculate the total number of books Henry donated
    donated_from_bookshelf = 3 * 15  # Henry filled 3 boxes of 15 books each from his bookshelf
    total_donated = donated_from_bookshelf + 21 + 4 + 18  # Henry donated books from different places in his home

    # Calculate the total number of books he took from the "free to a good home" box
    taken_from_box = 12

    # Calculate the remaining number of books Henry has
    total_books = 99
    remaining_books = total_books - (total_donated - taken_from_box)

    result = remaining_books
    return result

print(solution())