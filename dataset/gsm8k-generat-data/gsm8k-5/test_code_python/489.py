def solution():
    price_top = 8  # The "TOP" book costs $8
    price_abc = 23  # The "ABC" book costs $23
    qty_top = 13  # Thirteen "TOP" books were sold last week
    qty_abc = 4  # Four "ABC" books were sold last week

    # Calculate the earnings from selling the "TOP" books
    earnings_top = price_top * qty_top

    # Calculate the earnings from selling the "ABC" books
    earnings_abc = price_abc * qty_abc

    # Calculate the difference in earnings between the two books
    difference_earnings = earnings_top - earnings_abc
    result = difference_earnings
    return result

print(solution())