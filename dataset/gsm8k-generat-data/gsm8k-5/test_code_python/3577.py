def solution():
    race_distance = (7 * 3/4)  # Total distance of the race
    this_year_time = 42  # Time taken by this year's winner
    last_year_time = 47.25  # Time taken by last year's winner

    # Calculate the speed of the winners in miles per minute
    this_year_speed = race_distance / this_year_time
    last_year_speed = race_distance / last_year_time

    # Calculate the time taken to run 1 mile for both winners
    this_year_one_mile_time = 1 / this_year_speed
    last_year_one_mile_time = 1 / last_year_speed

    # Calculate the difference in minutes
    difference = last_year_one_mile_time - this_year_one_mile_time
    result = difference * 60  # Convert to minutes
    return result

print(solution())