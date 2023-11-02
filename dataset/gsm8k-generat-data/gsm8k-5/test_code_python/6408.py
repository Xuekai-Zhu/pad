def solution():
    total_time = 67  # Annie spent a total of 67 minutes on the diorama and planning it
    planning_time = (total_time + 5) / 3  # Solving for planning time using given formula
    building_time = total_time - planning_time  # Solving for building time

    result = building_time
    return result

print(solution())