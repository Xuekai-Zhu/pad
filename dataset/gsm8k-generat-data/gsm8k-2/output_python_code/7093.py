def solution():
    """Molly got a bike for her thirteenth birthday. She rode her bike 3 miles a day, every day, until she turned 16. How many miles did Molly ride on her bike?"""
    daily_distance = 3
    years_riding = 16 - 13
    total_distance = daily_distance * 365 * years_riding
    result = total_distance
    return result

print(solution())