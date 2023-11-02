def solution():
    """A single train car can carry 60 passengers. A 747 airplane can carry 366 passengers. How many more passengers can a train with 16 cars carry than 2 airplanes?"""
    # Define the capacity of a single train car and a 747 airplane
    train_car_capacity = 60
    airplane_capacity = 366

    # Calculate the total capacity of 16 train cars
    total_train_capacity = train_car_capacity * 16

    # Calculate the total capacity of 2 airplanes
    total_airplane_capacity = airplane_capacity * 2

    # Calculate the difference in capacity between the two options
    capacity_difference = total_train_capacity - total_airplane_capacity

    # return the result
    result = capacity_difference
    return result

print(solution())