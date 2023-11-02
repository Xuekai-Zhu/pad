def solution():
    # Initialize variables
    starting_squats = 30
    increase_per_day = 5
    days_in_future = 2

    # Calculate the number of squats on each day
    day1_squats = starting_squats
    day2_squats = starting_squats + increase_per_day
    day3_squats = starting_squats + (2 * increase_per_day)
    day4_squats = starting_squats + (3 * increase_per_day)

    # Calculate the number of squats on the day in the future
    squats_in_future = starting_squats + (days_in_future * increase_per_day)

    # Return the result
    result = squats_in_future
    return result

print(solution())