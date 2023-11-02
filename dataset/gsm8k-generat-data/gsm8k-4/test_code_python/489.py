def solution():
    """At a certain bookstore, the best-selling book, "TOP," costs $8. The least-selling book, "ABC," costs $23. Thirteen "TOP" books and four "ABC" books were sold last week. What is the difference in the bookstore's earnings on these two books last week?"""
    # Define the prices and quantities of the two books
    top_price = 8
    abc_price = 23
    top_quantity = 13
    abc_quantity = 4

    # Calculate the earnings from selling TOP books
    top_earnings = top_price * top_quantity

    # Calculate the earnings from selling ABC books
    abc_earnings = abc_price * abc_quantity

    # Calculate the difference in earnings
    earnings_difference = top_earnings - abc_earnings

    result = earnings_difference
    return result

print(solution())