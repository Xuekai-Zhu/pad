def solution():
    num_laps = 7
    town_square_length = 0.75
    this_year_time = 42
    last_year_time = 47.25

    # Calculate the total distance of the race
    total_distance = num_laps * town_square_length

    # Calculate the speed of this year's winner in miles per minute
    this_year_speed = total_distance / this_year_time

    # Calculate the speed of last year's winner in miles per minute
    last_year_speed = total_distance / last_year_time

    # Calculate the difference in speed between the two winners
    speed_difference = this_year_speed - last_year_speed

    # Calculate the time difference per mile between the two winners
    time_difference = 1 / speed_difference

    # Convert the time difference to minutes and round to 2 decimal places
    result = round(time_difference * 60, 2)
    return result

print(solution())