def solution():
    """Tracy has a charity book collection store from which she receives book donations from members of her town. Any person who wants to borrow a book is free to do so as long as they return the book after they've finished reading. She has already received 300 book donations. If ten people come and donate five books each in a week, and a total of 140 books are borrowed by other people to read, calculate the total number of books she has remaining in the store?"""
    initial_donations = 300
    new_donations = 10 * 5
    borrowed_books = 140
    remaining_books = initial_donations + new_donations - borrowed_books
    result = remaining_books
    return result

print(solution())