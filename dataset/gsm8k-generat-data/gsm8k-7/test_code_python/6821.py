def solution():
    days_worked = 5
    miles_per_day_to_work = 6
    dog_walks_per_day = 2
    daily_mileage = (miles_per_day_to_work * 2) + (dog_walks_per_day * 2)
    weekly_mileage = daily_mileage * days_worked

    weekly_mileage += 1  # add the mile to his best friend's house
    weekly_mileage += (2 * 3)  # add the miles to the convenience store
    result = weekly_mileage
    return result

print(solution())