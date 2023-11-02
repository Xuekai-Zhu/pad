def solution():
    # Calculate the time it takes for 3 kangaroos to travel across a highway
    time_kangaroos = 3 * 18  # 3 kangaroos traveling at the same speed a total of 18 hours

    # Calculate the time it takes for 4 turtles to travel across a highway
    time_turtles = 4 * (18 / 2)  # 4 turtles traveling at half the speed of a kangaroo to do

    # Calculate the total time it will take for all four turtles to travel across a highway
    total_time = time_kangaroos + time_turtles
    result = total_time
    return result

print(solution())