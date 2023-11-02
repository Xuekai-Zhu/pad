def solution():
    # Total number of tomatoes produced by first plant
    first_plant = 2 * 12  # 2 dozen tomatoes is 24

    # Total number of tomatoes produced by second plant
    second_plant = int((first_plant / 2) + 5)  # Half as many as first plant + 5

    # Total number of tomatoes produced by third plant
    third_plant = second_plant + 2

    # Total number of tomatoes produced by all three plants
    total_tomatoes = first_plant + second_plant + third_plant
    result = total_tomatoes
    return result

print(solution())