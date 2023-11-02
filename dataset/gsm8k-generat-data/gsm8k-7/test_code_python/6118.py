def solution():
    num_passengers_per_train_car = 60
    num_train_cars = 16
    num_passengers_per_airplane = 366
    num_airplanes = 2

    # Calculate the total number of passengers a train with 16 cars can carry
    total_train_passengers = num_passengers_per_train_car * num_train_cars

    # Calculate the total number of passengers 2 airplanes can carry
    total_airplane_passengers = num_passengers_per_airplane * num_airplanes

    # Calculate the difference in the number of passengers that can be carried
    difference = total_train_passengers - total_airplane_passengers
    result = difference
    return result

print(solution())