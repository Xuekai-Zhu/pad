def solution():
    total_people = 240
    ratio = 4
    
    # Calculate the ratio between Ryan's party and Taylor's party
    total_ratio = 1 + ratio
    
    # Calculate the number of people at Ryan's party
    ryan_party = (ratio / total_ratio) * total_people
    
    result = ryan_party
    return result

print(solution())