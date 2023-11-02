def solution():
    """Every morning Harry takes 15 minutes to buy coffee and a bagel and twice that long to read the paper and eat before going in to work. How long does Harry's morning routine take?"""
    # Define the time it takes to buy coffee and a bagel
    time_coffee_bagel = 15

    # Define the time it takes to read the paper and eat
    time_paper_eat = 2 * time_coffee_bagel

    # Calculate the total time of Harry's morning routine
    total_time = time_coffee_bagel + time_paper_eat

    # return the result
    result = total_time
    return result

print(solution())