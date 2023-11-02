def solution():
    """Sandra eats 3 beignets every morning. How many beignets will she eat in 16 weeks?"""
    # Define the number of weeks and beignets per day
    WEEKS = 16
    BEIGNETS_PER_DAY = 3

    # Calculate the total number of beignets eaten
    total_beignets = WEEKS * 7 * BEIGNETS_PER_DAY

    # Return the result
    result = total_beignets
    return result

print(solution())