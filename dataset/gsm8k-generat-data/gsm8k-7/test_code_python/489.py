def solution():
    top_price = 8
    abc_price = 23
    num_top_books_sold = 13
    num_abc_books_sold = 4

    # Calculate the earnings from selling "TOP" books
    top_earnings = top_price * num_top_books_sold

    # Calculate the earnings from selling "ABC" books
    abc_earnings = abc_price * num_abc_books_sold

    # Calculate the difference in earnings between the two books
    earnings_difference = top_earnings - abc_earnings
    result = earnings_difference
    return result

print(solution())