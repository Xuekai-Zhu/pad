def solution():
    wednesday_hours = 2
    thursday_hours = 2
    friday_additional_hours = 3

    # Calculate the total number of hours Max played on Friday
    friday_hours = wednesday_hours + friday_additional_hours

    # Calculate the total number of hours Max played in three days
    total_hours = wednesday_hours + thursday_hours + friday_hours

    # Calculate the average number of hours Max spent playing video games
    avg_hours = total_hours / 3
    result = avg_hours
    return result

print(solution())