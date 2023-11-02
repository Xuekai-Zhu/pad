def solution():
    
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