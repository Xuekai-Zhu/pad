def solution():
    
    agnes_age = 25
    jane_age = 6
    years = 0
    while agnes_age != jane_age * 2:
        years += 1
        agnes_age += 1
        jane_age += 1
    result = years
    return result

print(solution())