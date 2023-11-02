def solution():
    """To buy a book, you pay $20 for each of the first 5 books at the supermarket, and for each additional book you buy over $20, you receive a discount of $2. If Beatrice bought 20 books, how much did she pay at the supermarket?"""
    num_books = 20
    base_price = 20
    discount = 2
    total_price = 0
    for i in range(1, num_books+1):
        if i <= 5:
            total_price += base_price
        else:
            total_price += max(base_price - (i-5)*discount, 0)
    
    result = total_price
    return result

print(solution())