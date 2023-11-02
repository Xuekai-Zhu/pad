def solution():
    first_floor = 1
    up_first_time = 5
    down_first_time = 2
    up_second_time = 7
    top_distance = 9

    # Calculate Earl's position after going up and down the first time
    position_first_time = first_floor + up_first_time - down_first_time

    # Calculate Earl's position after going up the second time
    position_second_time = position_first_time + up_second_time

    # Calculate the total number of floors in the building
    total_floors = position_second_time + top_distance
    result = total_floors
    return result

print(solution())