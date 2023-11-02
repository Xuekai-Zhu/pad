def solution():
    """At a certain bookstore, the best-selling book, "TOP," costs $8. The least-selling book, "ABC," costs $23. Thirteen "TOP" books and four "ABC" books were sold last week. What is the difference in the bookstore's earnings on these two books last week?"""
    top_price = 8
    abc_price = 23
    top_sold = 13
    abc_sold = 4
    top_earnings = top_sold * top_price
    abc_earnings = abc_sold * abc_price
    difference = top_earnings - abc_earnings
    result = difference
    return result

print(solution())