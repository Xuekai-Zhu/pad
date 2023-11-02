def solution():
    """Joey wants to buy the latest released pair of designer High Jump basketball sneakers. He plans to mow 3 neighbors’ lawns for $8 a lawn, sell 2 collectible figures to his friends for $9 each, and work an after-school job for 10 hours at $5 per hour. If his earnings just cover the price of the High Jump sneakers, how much do the shoes cost?"""

    lawn_mowing_earnings = 3 * 8
    collectible_figures_earnings = 2 * 9
    after_school_job_earnings = 10 * 5
    total_earnings = lawn_mowing_earnings + collectible_figures_earnings + after_school_job_earnings
    sneaker_cost = total_earnings

    result = sneaker_cost
    return result

print(solution())