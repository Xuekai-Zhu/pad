def solution():
    total_books = 99
    donated_books = 3 * 15 + 21 + 4 + 18  # Total books donated
    taken_books = 12  # Books taken from the "free to a good home" box
    remaining_books = total_books - donated_books + taken_books
    result = remaining_books
    return result

print(solution())