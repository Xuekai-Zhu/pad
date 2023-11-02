def solution():
    wednesday_hours = 2  # Max played for 2 hours on Wednesday
    thursday_hours = 2  # Max played for 2 hours on Thursday
    friday_hours = wednesday_hours + 3  # Max spent over 3 hours more on playing on Friday than on Wednesday

    # Calculate the total hours Max spent playing video games during the three days
    total_hours = wednesday_hours + thursday_hours + friday_hours

    # Calculate the average hours per day
    average_hours = total_hours / 3
    result = average_hours
    return result

print(solution())