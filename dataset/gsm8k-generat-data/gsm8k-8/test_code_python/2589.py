def solution():
    # Calculate the total number of apples eaten by children
    children_apples = 33 * 10
    
    # Calculate the remaining apples for adults
    adult_apples = 450 - children_apples
    
    # Calculate the number of adults based on the number of apples they each ate
    num_adults = adult_apples / 3
    
    result = num_adults
    return result

print(solution())