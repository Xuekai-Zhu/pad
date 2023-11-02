def solution():
    car_time = 4.5  # time taken by car to reach station B
    train_time = car_time + 2  # train takes 2 hours longer than car

    # Let distance be D
    # Let speed of car be S_c and speed of train be S_t
    # Then we have: D / S_c = car_time and D / S_t = train_time
    # Solving for D in both equations, we get: D = S_c * car_time = S_t * train_time
    # Combining the equations, we get: S_c * car_time = S_t * (car_time + 2)
    # Simplifying, we get: S_t = S_c * (car_time / (train_time - car_time))

    # Assume that the distance is 1 unit (it can be any value since distance does not matter)
    distance = 1.0

    # Calculate the speed of the car
    speed_car = distance / car_time

    # Calculate the speed of the train
    speed_train = speed_car * (car_time / (train_time - car_time))

    # Calculate the total time taken
    combined_time = car_time + train_time
    result = combined_time
    return result

print(solution())