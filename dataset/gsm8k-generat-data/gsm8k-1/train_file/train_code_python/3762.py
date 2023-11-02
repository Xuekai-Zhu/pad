def solution():
    """Cooper makes 7 apple pies a day. He does this for 12 days. Ashley then eats 50 of his pies. How many apple pies remain with Cooper?"""
    pies_per_day = 7
    days = 12
    total_pies = pies_per_day * days
    pies_eaten = 50
    pies_remaining = total_pies - pies_eaten
    result = pies_remaining
    return result

print(solution())