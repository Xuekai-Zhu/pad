def solution():
    
    initial_goldfish = 18
    goldfish_lost_per_week = 5
    goldfish_gained_per_week = 3
    weeks = 7
    remaining_goldfish = initial_goldfish - (goldfish_lost_per_week * weeks)
    total_goldfish = remaining_goldfish + (goldfish_gained_per_week * weeks)
    result = total_goldfish
    return result

print(solution())