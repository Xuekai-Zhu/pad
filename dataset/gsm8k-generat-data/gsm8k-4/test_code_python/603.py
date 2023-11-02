def solution():
    """Alyssa and Abigail need to collect 100 empty cans for their Science project. As of today, Alyssa collected 30 while Abigail collected 43 empty cans. How many more empty cans should they collect?"""
    # Define the number of cans collected by Alyssa and Abigail
    alyssa_cans = 30
    abigail_cans = 43

    # Calculate the total number of cans collected
    total_cans = alyssa_cans + abigail_cans

    # Calculate the number of cans still needed
    cans_needed = 100 - total_cans

    # return the result
    result = cans_needed
    return result

print(solution())