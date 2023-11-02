def solution():
    """Alyssa and Abigail need to collect 100 empty cans for their Science project. As of today, Alyssa collected 30 while Abigail collected 43 empty cans. How many more empty cans should they collect?"""
    total_cans_needed = 100
    cans_collected_by_alyssa = 30
    cans_collected_by_abigail = 43
    cans_remaining = total_cans_needed - (cans_collected_by_alyssa + cans_collected_by_abigail)
    result = cans_remaining
    return result

print(solution())