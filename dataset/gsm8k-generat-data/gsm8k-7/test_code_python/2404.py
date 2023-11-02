def solution():
    tommy_cars = 3
    jessie_cars = 3
    total_cars = tommy_cars + jessie_cars  # total cars Tommy and Jessie have

    # Calculate the number of cars Jessie's older brother has
    jessie_brother_cars = total_cars + 5

    # Calculate the total number of cars the three of them have altogether
    total_cars_altogether = tommy_cars + jessie_cars + jessie_brother_cars
    result = total_cars_altogether
    return result

print(solution())