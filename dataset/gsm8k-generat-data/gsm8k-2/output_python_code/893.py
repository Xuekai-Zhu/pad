def solution():
    """Nick has 35 quarters. 2/5 of the quarters are state quarters, and 50 percent of the state quarters are Pennsylvania. How many Pennsylvania state quarters does Nick have?"""
    total_quarters = 35
    state_quarters = (2/5) * total_quarters
    pennsylvania_quarters = 0.5 * state_quarters
    result = pennsylvania_quarters
    return result

print(solution())