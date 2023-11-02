def solution():
    num_earrings = 4
    num_magnets_per_earring = 2
    
    num_buttons_per_earring = num_magnets_per_earring / 2
    
    num_gemstones_per_earring = num_buttons_per_earring * 3
    
    total_gemstones_needed = num_gemstones_per_earring * num_earrings
    result = total_gemstones_needed
    return result

print(solution())