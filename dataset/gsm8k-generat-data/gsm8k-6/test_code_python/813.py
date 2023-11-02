def solution():
    # Calculate the cost of two visits to the discount clinic
    cost_discount_clinic = 2 * (0.3 * 200)  # discount clinic is 70% cheaper than a normal doctor
    # Calculate the amount of money Tom saves
    savings = 2 * 200 - cost_discount_clinic
    result = savings
    return result

print(solution())