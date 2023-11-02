def solution():
    # Number of toy cars made yesterday
    yesterday_cars = 60

    # Number of toy cars made today (twice the number made yesterday)
    today_cars = 2 * yesterday_cars

    # Total number of toy cars made in the two days
    total_cars = yesterday_cars + today_cars
    result = total_cars
    return result

print(solution())