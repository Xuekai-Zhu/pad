def solution():
    # Define the total time spent on the diorama
    total_time = 67

    # Calculate the amount of time spent planning
    planning_time = (total_time + 5) / 3

    # Calculate the amount of time spent building
    building_time = total_time - planning_time
    result = building_time
    return result

print(solution())