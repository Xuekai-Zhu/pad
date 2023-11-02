def solution():
    """Emily spent X dollars on Friday, twice that amount on Saturday, and then three times X on Sunday. Over the three days, she spent $120. What is the value of X, in dollars?"""
    # Define the amount spent on Friday as X
    X = 0

    # Calculate the amounts spent on Saturday and Sunday
    saturday_spending = 2 * X
    sunday_spending = 3 * X

    # Calculate the total spending over the three days
    total_spending = X + saturday_spending + sunday_spending

    # Set the total spending to be equal to $120, and solve for X
    X = 120 / 6

    # Display the value of X
    result = X
    return result

print(solution())