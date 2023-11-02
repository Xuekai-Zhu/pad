def solution():
    
    total_people = 240
    ratio = 4
    ryan_ratio = ratio / (1 + ratio)
    ryan_people = ryan_ratio * total_people
    result = ryan_people
    return result

print(solution())