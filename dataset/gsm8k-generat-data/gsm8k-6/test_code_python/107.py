def solution():
    # Calculate the total number of cars that pass Happy Street from Monday through Sunday
    monday_cars = 0.8 * 25  # 20% less than Tuesday
    wednesday_cars = monday_cars + 2  # 2 more cars than Monday
    weekday_cars = monday_cars + tuesday_cars + wednesday_cars + 10 + 10  # Thursday and Friday each have 10 cars
    weekend_cars = 5 * 2  # 5 cars per day on weekends
    total_cars = weekday_cars + weekend_cars
    result = total_cars
    return result

print(solution())