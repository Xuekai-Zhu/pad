def solution():
    
    total_cases = 250
    first_house_ratio = 1/2
    second_house_ratio = 1 + first_house_ratio
    third_house_ratio = 2
    first_house_cases = second_house_ratio * first_house_cases
    third_house_cases = first_house_cases * third_house_ratio
    result = third_house_cases
    return result

print(solution())