def solution():
    # Define the ratios
    green_to_red_ratio = 4
    red_to_purple_ratio = 6

    # Set up equations based on the ratios
    green_cars = green_to_red_ratio * red_cars
    red_cars = purple_cars + red_to_purple_ratio
    total_cars = green_cars + red_cars + purple_cars

    # Solve for the number of purple cars
    purple_cars = (total_cars - red_cars - green_cars) / 2

    result = purple_cars
    return result

print(solution())