def solution():
    lawn_mowing_income = 3 * 8  # Joey earns $8 per lawn for mowing 3 neighbors' lawns
    collectible_income = 2 * 9  # Joey earns $9 per collectible figure for selling 2 figures to his friends
    after_school_income = 10 * 5  # Joey earns $5 per hour for working 10 hours at his after-school job
    total_income = lawn_mowing_income + collectible_income + after_school_income

    # Assume the price of the High Jump sneakers is equal to Joey's total income
    sneaker_price = total_income
    result = sneaker_price
    return result

print(solution())