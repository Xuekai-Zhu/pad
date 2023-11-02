def solution():
    train_car_capacity = 60  # Capacity of a single train car
    train_cars = 16  # Number of train cars
    train_capacity = train_car_capacity * train_cars  # Total capacity of the train

    airplane_capacity = 366  # Capacity of a single airplane
    num_airplanes = 2  # Number of airplanes
    airplane_total_capacity = airplane_capacity * num_airplanes  # Total capacity of the airplanes

    # Calculate the difference in capacity between the train and the airplanes
    capacity_difference = train_capacity - airplane_total_capacity
    result = capacity_difference
    return result

print(solution())