def solution():
    
    starting_goldfish = 18
    goldfish_lost_per_week = 5
    goldfish_gained_per_week = 3
    weeks = 7
    goldfish_remaining = starting_goldfish - (goldfish_lost_per_week * weeks) + (goldfish_gained_per_week * weeks)
    result = goldfish_remaining
    return result

print(solution())