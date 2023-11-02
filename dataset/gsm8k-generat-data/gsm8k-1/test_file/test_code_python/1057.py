def solution():
    """Betsy and Donovan made a meal together. Betsy's part took 18 minutes longer than Donovan's part. The meal was made in 98 minutes. How many minutes long was Betsy's part?"""
    total_time = 98
    b_time = d_time + 18
    d_time = (total_time - b_time) / 2
    b_time = total_time - d_time
    result = b_time
    return result

print(solution())