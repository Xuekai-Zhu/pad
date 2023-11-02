def solution():
    longest_book = 396
    shortest_book = longest_book / 4
    middle_book = shortest_book * 3

    pages_arranged = [longest_book, middle_book, shortest_book]
    middle_book_pages = sorted(pages_arranged)[1]

    result = middle_book_pages
    return result

print(solution())