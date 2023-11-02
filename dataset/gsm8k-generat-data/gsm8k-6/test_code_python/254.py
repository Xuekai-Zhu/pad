def solution():
    # Calculate the number of cars in each section and the total number of rows
    cars_in_G = 15 * 10
    cars_in_H = 20 * 9
    total_rows = 15 + 20

    # Calculate the total number of cars Nate walked past
    total_cars = cars_in_G + cars_in_H

    # Calculate the number of minutes Nate spent searching the parking lot
    minutes = total_cars / 11
    result = minutes
    return result

print(solution())