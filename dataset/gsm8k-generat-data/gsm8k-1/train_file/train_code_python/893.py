def solution():
    """Nick has 35 quarters. 2/5 of the quarters are state quarters, and 50 percent of the state quarters are Pennsylvania. How many Pennsylvania state quarters does Nick have?"""
    total_quarters = 35
    state_quarters = total_quarters * (2/5)
    pa_quarters = state_quarters * 0.5
    result = pa_quarters
    return result

print(solution())