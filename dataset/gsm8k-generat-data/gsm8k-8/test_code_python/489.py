def solution():
    # Define the cost and quantity of each book
    top_cost = 8
    abc_cost = 23
    top_quantity = 13
    abc_quantity = 4

    # Calculate the total earnings for each book
    top_earnings = top_cost * top_quantity
    abc_earnings = abc_cost * abc_quantity

    # Calculate the difference in earnings between the two books
    earnings_difference = top_earnings - abc_earnings
    result = earnings_difference
    return result

print(solution())