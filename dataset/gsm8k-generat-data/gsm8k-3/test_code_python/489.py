def solution():
    """At a certain bookstore, the best-selling book, "TOP," costs $8. The least-selling book, "ABC," costs $23. Thirteen "TOP" books and four "ABC" books were sold last week. What is the difference in the bookstore's earnings on these two books last week?"""
    # Define the cost and sales of each type of book
    TOP_COST = 8
    ABC_COST = 23
    TOP_SALES = 13
    ABC_SALES = 4

    # Calculate the total earnings from each type of book
    top_earnings = TOP_COST * TOP_SALES
    abc_earnings = ABC_COST * ABC_SALES

    # Calculate the difference in earnings
    earnings_diff = top_earnings - abc_earnings

    # Display the earnings difference
    result = earnings_diff
    return result

print(solution())