def solution():
    """Candice read 3 times as many books as Amanda in their school's Book Tournament. Kara read half the number of books that Amanda read, and Patricia read 7 times the number of books that Kara read. If Candice read 18 books, how many books did Patricia read?"""
    # Define the number of books Candice read
    candice_books = 18

    # Calculate the number of books Amanda read
    amanda_books = candice_books / 3

    # Calculate the number of books Kara read
    kara_books = amanda_books / 2

    # Calculate the number of books Patricia read
    patricia_books = kara_books * 7

    # return the result
    result = patricia_books
    return result

print(solution())