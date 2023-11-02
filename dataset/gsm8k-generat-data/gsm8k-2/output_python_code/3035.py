def solution():
    """A yearly book sale is held in school where students can sell their old books at a cheaper price. Two-fifths of Lovely's books can be sold for $2.50 each and the rest for $2 each. How much will Lovely earn if all 10 books were sold?"""
    total_books = 10
    fraction_high_price = 2/5
    high_price_books = fraction_high_price * total_books
    low_price_books = total_books - high_price_books
    high_price = 2.5
    low_price = 2
    total_earnings = (high_price_books * high_price) + (low_price_books * low_price)
    result = total_earnings
    return result

print(solution())