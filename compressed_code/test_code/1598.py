def solution():
    
    wipes_per_day = 2
    days = 360
    total_wipes_needed = wipes_per_day * days
    wipes_per_pack = 120
    packs_needed = total_wipes_needed / wipes_per_pack
    result = packs_needed
    return result

print(solution())