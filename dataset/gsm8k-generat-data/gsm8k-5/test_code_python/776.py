def solution():
    amber_hours = 12  # Amber worked for 12 hours
    armand_hours = amber_hours / 3  # Armand worked one-third as long as Amber
    ella_hours = amber_hours * 2  # Ella worked twice as long as Amber

    # Calculate the total number of hours worked by the three people
    total_hours = amber_hours + armand_hours + ella_hours
    result = total_hours
    return result

print(solution())