def solution():
    """You have 32$ to spend on groceries.  You buy a loaf of bread for 3$, a candy bar for 2$, and 1/3 of whats left on a Turkey.  How much money do you have left?"""
    # Define the starting budget
    budget = 32

    # Subtract the cost of the bread and candy bar
    budget -= 3 + 2

    # Calculate 1/3 of the remaining budget for the turkey
    turkey_cost = budget / 3

    # Subtract the cost of the turkey
    budget -= turkey_cost

    # Display the remaining budget
    result = budget
    return result

print(solution())