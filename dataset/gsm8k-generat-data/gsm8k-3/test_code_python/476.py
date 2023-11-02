def solution():
    """Joey wants to buy the latest released pair of designer High Jump basketball sneakers. He plans to mow 3 neighbors’ lawns for $8 a lawn, sell 2 collectible figures to his friends for $9 each, and work an after-school job for 10 hours at $5 per hour. If his earnings just cover the price of the High Jump sneakers, how much do the shoes cost?"""
    # Define the prices and earnings for each activity
    LAWN_MOWING_PRICE = 8
    COLLECTIBLE_FIGURE_PRICE = 9
    AFTER_SCHOOL_JOB_RATE = 5
    AFTER_SCHOOL_JOB_HOURS = 10

    # Calculate Joey's earnings from each activity
    lawn_mowing_earnings = 3 * LAWN_MOWING_PRICE
    collectible_figure_earnings = 2 * COLLECTIBLE_FIGURE_PRICE
    after_school_job_earnings = AFTER_SCHOOL_JOB_RATE * AFTER_SCHOOL_JOB_HOURS

    # Calculate Joey's total earnings
    total_earnings = lawn_mowing_earnings + collectible_figure_earnings + after_school_job_earnings

    # Calculate the cost of the High Jump sneakers
    sneakers_cost = total_earnings

    # Display the cost of the High Jump sneakers
    result = sneakers_cost
    return result

print(solution())