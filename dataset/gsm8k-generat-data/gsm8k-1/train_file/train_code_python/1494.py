def solution():
    """In a bookstore, a book costs $5. When Sheryll bought 10 books, she was given a discount of $0.5 each. How much did Sheryll pay in all?"""
    book_cost = 5
    discount = 0.5
    num_books = 10
    total_cost = (num_books * book_cost) - (discount * num_books)
    result = total_cost
    return result

print(solution())