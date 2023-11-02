def solution():
    """Molly got a bike for her thirteenth birthday. She rode her bike 3 miles a day, every day, until she turned 16. How many miles did Molly ride on her bike?"""
    years_ridden = 16 - 13
    miles_ridden_per_day = 3
    total_miles_ridden = years_ridden * 365 * miles_ridden_per_day
    result = total_miles_ridden
    return result

print(solution())