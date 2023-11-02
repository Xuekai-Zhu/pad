def solution():
    
    mms_per_sundae_monday = 6
    mms_per_sundae_tuesday = 10 
    total_sundaes = 40 + 20
    total_mms = (40 * mms_per_sundae_monday) + (20 * mms_per_sundae_tuesday)
    packs_needed = total_mms / 40
    result = packs_needed
    return result

print(solution())