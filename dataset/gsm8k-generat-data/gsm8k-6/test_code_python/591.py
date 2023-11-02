def solution():
    # Find the total number of cherries needed
    total_cherries = 3 * 80  # 3 pounds of cherries with 80 single cherries in one pound

    # Find the number of cherries that can be pitted in one minute
    cherries_per_minute = 20/10  # 20 cherries take 10 minutes to pit

    # Find the total number of minutes to pit all the cherries
    total_minutes = total_cherries / cherries_per_minute

    # Convert minutes to hours
    total_hours = total_minutes / 60

    result = total_hours
    return result

print(solution())