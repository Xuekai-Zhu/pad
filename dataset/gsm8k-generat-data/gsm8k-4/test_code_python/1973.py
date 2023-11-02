def solution():
    """Emily spent X dollars on Friday, twice that amount on Saturday, and then three times X on Sunday. Over the three days, she spent $120. What is the value of X, in dollars?"""
    # Define the amount spent on each day in terms of X
    friday_spending = X
    saturday_spending = 2 * X
    sunday_spending = 3 * X

    # Calculate the total spending over the three days
    total_spending = friday_spending + saturday_spending + sunday_spending

    # Set the total spending equal to $120 and solve for X
    # X + 2X + 3X = 120
    # 6X = 120
    # X = 20

    X = 20

    # Return the result
    result = X
    return result

print(solution())