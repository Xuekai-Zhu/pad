def solution():
    car_wash_time = 10  # in minutes
    oil_change_time = 15  # in minutes
    tire_change_time = 30  # in minutes
    num_cars_washed = 9
    num_cars_oil_changed = 6
    num_tire_changes = 2

    # Calculate the total time Mike spent working
    total_time = (car_wash_time * num_cars_washed + 
                  oil_change_time * num_cars_oil_changed + 
                  tire_change_time * num_tire_changes) / 60  # convert to hours
    result = total_time
    return result

print(solution())