def solution():
    longest_book = 396
    shortest_book = longest_book / 4
    middle_book = shortest_book * 3

    # Put the number of pages of each book in a list
    book_list = [longest_book, middle_book, shortest_book]

    # Sort the list in descending order
    book_list.sort(reverse=True)

    # Middle book is the 2nd element in the sorted list
    middle_book_pages = book_list[1]
    return middle_book_pages

print(solution())