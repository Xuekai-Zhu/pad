def solution():
    """A train takes 2 hours longer to go an equal distance of a car. If the car and the train leave station A at the same time, and the car reaches station B 4.5 hours later, calculate the combined time the car and the train take to reach station B."""
    # Define the time taken by the car to reach station B
    car_time = 4.5

    # Define the time taken by the train to cover the same distance as the car
    train_extra_time = 2

    # Calculate the speed of the car
    car_speed = 1 / car_time

    # Calculate the speed of the train
    train_speed = car_speed / (1 + train_extra_time / car_time)

    # Calculate the time taken by the train to reach station B
    train_time = 1 / train_speed

    # Calculate the combined time taken by the car and the train to reach station B
    total_time = car_time + train_time

    result = total_time
    return result

print(solution())