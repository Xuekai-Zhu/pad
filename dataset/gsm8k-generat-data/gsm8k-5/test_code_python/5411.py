def solution():
    car_time = 4.5  # time taken by the car to reach station B
    train_time = car_time + 2  # time taken by the train to cover equal distance
    combined_time = car_time + train_time  # total time taken by car and train to reach station B
    result = combined_time
    return result

print(solution())