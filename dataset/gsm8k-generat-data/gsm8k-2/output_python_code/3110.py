def solution():
    """John decides to get a new apartment with a roommate. His former rent was $2 per square foot for a 750 square foot apartment. His new apartment cost $2800 per month, which he splits evenly with the roommate. How much money does he save a year?"""
    old_rent = 2 * 750  # $/sqft * sqft
    new_rent = 2800 / 2  # split evenly with roommate
    savings_per_month = old_rent - new_rent
    savings_per_year = savings_per_month * 12
    result = savings_per_year
    return result

print(solution())