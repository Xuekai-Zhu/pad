def solution():
    total_cars = 20
    automatic_cars = 12
    manual_cars = 4

    # Calculate the number of semi-automatic cars
    semi_automatic_cars = total_cars - automatic_cars - manual_cars

    # Calculate the percentage of semi-automatic cars
    semi_automatic_percentage = (semi_automatic_cars / total_cars) * 100
    result = semi_automatic_percentage
    return result

print(solution())