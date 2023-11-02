def solution():
    
    num_people = 1 + 1 + 1 + 2 + 4 + 2 + 3
    num_beds = 4
    num_tents = (num_people - num_beds) / 2
    result = num_tents
    return result

print(solution())