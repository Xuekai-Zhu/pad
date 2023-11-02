def solution():
    """John pays for half the cost of raising a child. It costs $10,000 a year for the first 8 years and then twice that much per year until the child is 18. University tuition then costs $250,000. How much did it cost?"""
    first_8_years_cost = 8 * 10000
    remaining_years_cost = sum([2 * 10000 * i for i in range(9, 19)])
    university_cost = 250000
    total_cost = (first_8_years_cost + remaining_years_cost + university_cost) * 2
    result = total_cost
    return result

print(solution())