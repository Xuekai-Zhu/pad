def solution():
    # Calculate the total number of cherries
    total_cherries = 3 * 80

    # Calculate the total number of groups of 20 cherries that need to be pitted
    groups_of_20 = total_cherries / 20

    # Calculate the total number of minutes it will take to pit all the cherries
    total_time_minutes = groups_of_20 * 10

    # Convert the total time to hours
    total_time_hours = total_time_minutes / 60

    result = total_time_hours
    return result

print(solution())