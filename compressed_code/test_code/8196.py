def solution():
    
    total_books = 10
    fraction_of_books_sold_at_higher_price = 2 / 5
    fraction_of_books_sold_at_lower_price = 1 - fraction_of_books_sold_at_higher_price
    price_of_higher_priced_books = 2.5
    price_of_lower_priced_books = 2
    earnings_from_higher_priced_books = fraction_of_books_sold_at_higher_price * total_books * price_of_higher_priced_books
    earnings_from_lower_priced_books = fraction_of_books_sold_at_lower_price * total_books * price_of_lower_priced_books
    total_earnings = earnings_from_higher_priced_books + earnings_from_lower_priced_books
    result = total_earnings
    
    return result

print(solution())