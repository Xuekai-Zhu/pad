def solution():
    """John pays for half the cost of raising a child. It cost $10,000 a year for the first 8 years and then twice that much per year until the child is 18. University tuition then costs $250,000. How much did it cost?"""
    first_eight_years = 8 * 10000
    after_eight_years = (18 - 8) * 2 * 10000
    tuition_cost = 250000
    total_cost = (first_eight_years + after_eight_years + tuition_cost) * 2
    result = total_cost
    return result

print(solution())