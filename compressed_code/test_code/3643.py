def solution():
    
    starting_meat = 20
    meatballs = starting_meat * (1/4)
    spring_rolls = 3
    remaining_meat = starting_meat - meatballs - spring_rolls
    result = remaining_meat
    return result

print(solution())