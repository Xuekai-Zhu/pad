def solution():
    """Joey wants to buy the latest released pair of designer High Jump basketball sneakers. He plans to mow 3 neighbors’ lawns for $8 a lawn, sell 2 collectible figures to his friends for $9 each, and work an after-school job for 10 hours at $5 per hour. If his earnings just cover the price of the High Jump sneakers, how much do the shoes cost?"""
    # Calculate Joey's earnings from mowing lawns
    lawn_earnings = 3 * 8

    # Calculate Joey's earnings from selling collectible figures
    figure_earnings = 2 * 9

    # Calculate Joey's earnings from his after-school job
    job_earnings = 10 * 5

    # Calculate Joey's total earnings
    total_earnings = lawn_earnings + figure_earnings + job_earnings

    # Calculate the cost of the High Jump sneakers
    sneakers_cost = total_earnings

    result = sneakers_cost
    return result

print(solution())