def solution():
    """One-half of a pound of mangoes costs $0.60. How many pounds can Kelly buy with $12?"""
    # Define the cost of half a pound of mangoes and the total amount Kelly has to spend
    MANGO_COST = 0.60
    TOTAL_SPENDING = 12

    # Calculate the cost of one pound of mangoes
    one_pound_cost = MANGO_COST * 2

    # Calculate the amount of pounds Kelly can buy
    pounds = TOTAL_SPENDING / one_pound_cost

    # Return the result rounded to 2 decimal places
    result = round(pounds, 2)
    return result

print(solution())