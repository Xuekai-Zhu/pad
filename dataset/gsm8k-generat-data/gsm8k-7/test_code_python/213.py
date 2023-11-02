def solution():
    morning_mike = 50
    morning_ted = 2 * morning_mike
    afternoon_mike = 60
    afternoon_ted = afternoon_mike - 20

    # Calculate the total number of tomato seeds planted by Mike and Ted in the morning
    morning_total = morning_mike + morning_ted

    # Calculate the total number of tomato seeds planted by Mike and Ted in the afternoon
    afternoon_total = afternoon_mike + afternoon_ted

    # Calculate the total number of tomato seeds planted by Mike and Ted altogether
    total_seeds_planted = morning_total + afternoon_total
    result = total_seeds_planted
    return result

print(solution())