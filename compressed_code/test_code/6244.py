def solution():
    
    total_cans_needed = 100
    cans_collected_by_alyssa = 30
    cans_collected_by_abigail = 43
    cans_remaining = total_cans_needed - (cans_collected_by_alyssa + cans_collected_by_abigail)
    result = cans_remaining
    return result

print(solution())