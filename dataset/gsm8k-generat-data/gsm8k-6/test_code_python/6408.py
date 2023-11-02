def solution():
    # Convert the given time in minutes to hours
    total_time = 67 / 60  # the total time spent on the diorama
    planning_time = (total_time + 5/60) / 3  # the time spent on planning
    building_time = total_time - planning_time  # the time spent on building

    # Convert the building time back to minutes
    result = building_time * 60
    return result

print(solution())