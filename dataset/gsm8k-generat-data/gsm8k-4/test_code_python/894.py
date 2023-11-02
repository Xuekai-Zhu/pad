def solution():
    """Nick has 35 quarters. 2/5 of the quarters are state quarters, and 50 percent of the state quarters are Pennsylvania. How many Pennsylvania state quarters does Nick have?"""
    # Define the total number of quarters
    total_quarters = 35

    # Calculate the number of state quarters
    state_quarters = total_quarters * (2/5)

    # Calculate the number of Pennsylvania state quarters
    penn_quarters = state_quarters * 0.5

    # return the result
    result = penn_quarters
    return result

print(solution())