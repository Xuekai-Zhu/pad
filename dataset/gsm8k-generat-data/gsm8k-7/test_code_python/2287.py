def solution():
    green_cars = 4
    red_cars = 1
    purple_cars = 1

    # Calculate the number of red cars relative to purple cars
    red_cars = purple_cars + 6
    total_cars = purple_cars + red_cars + (green_cars * red_cars)

    # Calculate the number of purple cars
    purple_cars = (total_cars - red_cars - (green_cars * red_cars)) / 2

    result = purple_cars
    return result

print(solution())