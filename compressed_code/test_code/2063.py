def solution():
    
    total_ratio = 4 + 3 + 7
    halima_ratio = 4 / total_ratio
    beckham_ratio = 3 / total_ratio
    michelle_ratio = 7 / total_ratio
    total_age = 126
    halima_age = halima_ratio * total_age
    beckham_age = beckham_ratio * total_age
    age_difference = halima_age - beckham_age
    result = age_difference
    return result

print(solution())