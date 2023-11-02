def solution():
    week1_hours = 8
    week2_hours = 10
    week3_hours = 12

    # Calculate the total number of hours watched in three weeks
    total_hours = week1_hours + week2_hours + week3_hours

    # Calculate the average number of hours watched per week
    avg_hours = total_hours / 3
    result = avg_hours
    return result

print(solution())