def solution():
    total_goldfish = 100
    goldfish_allowed = total_goldfish / 2
    goldfish_caught = (goldfish_allowed / 5) * 3
    goldfish_remaining = goldfish_allowed - goldfish_caught
    result = goldfish_remaining 
    return result

print(solution())