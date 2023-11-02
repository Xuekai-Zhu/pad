def solution():
    
    total_apples = 450
    children = 33
    children_apples = children * 10
    adult_apples = total_apples - children_apples
    adult_apples_per_person = 3
    num_adults = adult_apples // (adult_apples_per_person)
    result = num_adults
    return result

print(solution())