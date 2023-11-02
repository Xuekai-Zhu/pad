def solution():
    """Nick has 35 quarters.  2/5 of the quarters are state quarters, and 50 percent of the state quarters are Pennsylvania.  How many Pennsylvania state quarters does Nick have?"""
    # Define the number of quarters Nick has
    quarters = 35

    # Calculate the number of state quarters and Pennsylvania state quarters
    state_quarters = quarters * 2/5
    pa_quarters = state_quarters * 0.5

    # Display the number of Pennsylvania state quarters Nick has
    result = pa_quarters
    return result

print(solution())