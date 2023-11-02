def solution():
    # Define the number of cars made yesterday
    yesterday_cars = 60

    # Calculate the number of cars made today
    today_cars = 2 * yesterday_cars

    # Calculate the total number of cars made
    total_cars = yesterday_cars + today_cars

    result = total_cars
    return result

print(solution())