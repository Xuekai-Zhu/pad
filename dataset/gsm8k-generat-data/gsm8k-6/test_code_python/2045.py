def solution():
    subway_time = 10  # hours spent on the subway
    train_time = 2 * subway_time  # time spent on the train is twice the subway time
    bike_time = 8  # hours spent biking
    total_time = subway_time + train_time + bike_time  # total time to reach Bronx
    result = total_time
    return result

print(solution())