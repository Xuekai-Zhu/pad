def solution():
    boris_books = 24
    boris_donated = boris_books / 4

    cameron_books = 30
    cameron_donated = cameron_books / 3

    total_books = boris_books + cameron_books - boris_donated - cameron_donated
    result = total_books
    return result

print(solution())