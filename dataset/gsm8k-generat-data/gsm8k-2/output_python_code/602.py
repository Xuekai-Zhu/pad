def solution():
    """Alyssa and Abigail need to collect 100 empty cans for their Science project. As of today, Alyssa collected 30 while Abigail collected 43 empty cans. How many more empty cans should they collect?"""
    current_collective_total = 30 + 43
    cans_left_to_collect = 100 - current_collective_total
    result = cans_left_to_collect
    return result

print(solution())