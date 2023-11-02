def solution():
    
    magnets_per_earring = 2
    buttons_per_earring = magnets_per_earring / 2
    gemstones_per_earring = buttons_per_earring * 3
    earrings_per_set = 2
    total_gemstones = gemstones_per_earring * earrings_per_set * 4
    result = total_gemstones
    return result

print(solution())