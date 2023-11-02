def solution():
    # Calculate the total number of cars that passed the toll booth on Monday and Tuesday
    monday_cars = 50
    tuesday_cars = monday_cars
    total_mon_tues_cars = monday_cars + tuesday_cars

    # Calculate the number of cars that passed the toll booth on Wednesday and Thursday
    wednesday_cars = 2 * monday_cars
    thursday_cars = 2 * monday_cars
    total_wed_thurs_cars = wednesday_cars + thursday_cars

    # Calculate the total number of cars that passed the toll booth on the remaining days of the week
    remaining_days_cars = 450 - total_mon_tues_cars - total_wed_thurs_cars

    # Calculate the number of cars that passed the toll booth on each of the remaining days
    each_remaining_day_cars = remaining_days_cars / 3

    result = each_remaining_day_cars
    return result

print(solution())