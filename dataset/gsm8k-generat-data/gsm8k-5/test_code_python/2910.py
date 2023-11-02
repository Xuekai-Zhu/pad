def solution():
    # Calculate the number of trains that come in an hour
    trains_per_hour = 60 // 5  # 60 minutes divided by the time between trains (5 minutes)

    # Calculate the total number of passengers who step on and off a train at the station in an hour
    passengers_per_train = 200 + 320  # Total number of passengers who step on and off a train at the station
    total_passengers = passengers_per_train * trains_per_hour

    # Calculate the number of different passengers who step on and off a train at the station in an hour
    different_passengers = passengers_per_train * 2  # Each passenger steps on and off a train
    total_different_passengers = different_passengers * trains_per_hour
    result = total_different_passengers
    return result

print(solution())