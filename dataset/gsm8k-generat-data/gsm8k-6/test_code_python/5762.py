def solution():
    # Calculate the total number of lice checks and the time it will take to complete them
    total_checks = 26 + 19 + 20 + 25  # sum of all the students in each grade level
    time_in_minutes = total_checks * 2  # each check takes 2 minutes
    time_in_hours = time_in_minutes / 60  # convert minutes to hours
    result = time_in_hours
    return result

print(solution())