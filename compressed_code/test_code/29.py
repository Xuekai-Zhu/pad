def solution():
    
    mom_cup_size = 8
    tea_ratio = 1 / mom_cup_size
    party_size = 12
    guest_cup_size = 6
    total_tea_needed = party_size * guest_cup_size * tea_ratio
    result = total_tea_needed
    return result

print(solution())