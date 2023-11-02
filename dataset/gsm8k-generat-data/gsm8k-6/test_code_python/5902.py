def solution():
    # Calculate the total number of tomatoes produced by the three plants
    tomatoes_first_plant = 2 * 12  # 2 dozen tomatoes
    tomatoes_second_plant = int((0.5 * tomatoes_first_plant) + 5)  # 5 more than half as many as the first plant
    tomatoes_third_plant = tomatoes_second_plant + 2  # 2 more than the second plant
    total_tomatoes = tomatoes_first_plant + tomatoes_second_plant + tomatoes_third_plant
    result = total_tomatoes
    return result

print(solution())