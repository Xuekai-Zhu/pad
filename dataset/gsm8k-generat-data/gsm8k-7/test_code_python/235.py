def solution():
    trains_per_birthday = 1
    trains_per_christmas = 2
    num_years = 5

    # Calculate the total number of trains received for birthdays over 5 years
    num_birthday_trains = trains_per_birthday * num_years

    # Calculate the total number of trains received for Christmases over 5 years
    num_christmas_trains = trains_per_christmas * 2 * num_years

    # Calculate the total number of trains received over 5 years
    total_trains = num_birthday_trains + num_christmas_trains

    # Double the total number of trains to find out how many he has now
    num_trains_now = total_trains * 2
    result = num_trains_now
    return result

print(solution())