def solution():
    # Calculate the number of hours each person worked
    amber_hours = 12
    armand_hours = amber_hours / 3
    ella_hours = amber_hours * 2

    # Calculate the total number of hours the 3 people worked
    total_hours = amber_hours + armand_hours + ella_hours
    result = total_hours
    return result

print(solution())