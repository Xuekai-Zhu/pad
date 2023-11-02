def solution():
    num_rows_g = 15
    num_cars_per_row_g = 10
    num_rows_h = 20
    num_cars_per_row_h = 9
    cars_per_minute = 11

    # Calculate the total number of cars in section G
    num_cars_g = num_rows_g * num_cars_per_row_g

    # Calculate the total number of cars in section H
    num_cars_h = num_rows_h * num_cars_per_row_h

    # Calculate the total number of cars Nate had to walk past
    total_cars = num_cars_g + num_cars_h

    # Calculate the total number of minutes Nate spent searching the parking lot
    total_minutes = total_cars / cars_per_minute
    result = total_minutes
    return result

print(solution())