def solution():
    """Joey wants to buy the latest released pair of designer High Jump basketball sneakers. He plans to mow 3 neighbors’ lawns for $8 a lawn, sell 2 collectible figures to his friends for $9 each, and work an after-school job for 10 hours at $5 per hour. If his earnings just cover the price of the High Jump sneakers, how much do the shoes cost?"""
    lawn_mowing_income = 8 * 3
    figures_income = 9 * 2
    after_school_job_income = 5 * 10
    total_income = lawn_mowing_income + figures_income + after_school_job_income
    sneaker_price = total_income
    result = sneaker_price
    return result

print(solution())