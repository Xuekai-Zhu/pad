def solution():
    # Calculate the distance of the race
    distance = 7 * (3/4)  # the town square is 3/4 of a mile long and the race is 7 times around

    # Calculate the speed of this year's winner in miles per hour
    speed_this_year = distance / (42/60)  # convert minutes to hours

    # Calculate the speed of last year's winner in miles per hour
    speed_last_year = distance / (47.25/60)  # convert minutes to hours

    # Calculate the time difference in minutes for one mile of the race
    time_diff = (1 / speed_last_year - 1 / speed_this_year) * 60

    result = round(time_diff, 2)  # round to 2 decimal places
    return result

print(solution())