def solution():
    weeknight_hours = 2  # Paul has 2 hours of homework on weeknights
    weekend_hours = 5  # Paul has 5 hours of homework for the entire weekend
    nights_without_homework = 2  # Paul has practice 2 nights out of the week and can't do any homework those nights
    remaining_weeknights = 5 - nights_without_homework  # Paul has 5 weeknights in total, but can't do homework on 2

    # Calculate the total homework Paul needs to do for the week
    total_homework = (weeknight_hours * remaining_weeknights) + weekend_hours

    # Calculate the average number of homework hours Paul needs to do on the remaining weeknights
    remaining_homework = total_homework - (weeknight_hours * nights_without_homework)
    remaining_nights = 5 - nights_without_homework
    average_homework_per_night = remaining_homework / remaining_nights
    result = average_homework_per_night
    return result

print(solution())