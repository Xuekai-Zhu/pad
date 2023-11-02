def solution():
    """To buy a book, you pay $20 for each of the first 5 books at the supermarket, and for each additional book you buy over $20, you receive a discount of $2. If Beatrice bought 20 books, how much did she pay at the supermarket?"""
    base_price = 20
    num_books = 20
    discount = 2
    books_over_discount = num_books - 5
    total_price = base_price * 5  # first 5 books at $20 each
    if books_over_discount > 0:
        total_price += (books_over_discount * (base_price - discount))
    result = total_price
    return result

print(solution())