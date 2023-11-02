def solution():
    # Calculate the total number of trains that come in an hour
    trains_in_hour = 60 // 5

    # Calculate the total number of passengers who step on and off in an hour
    passengers_per_train = 200 + 320
    total_passengers = passengers_per_train * trains_in_hour

    # Calculate the number of different passengers who step on and off
    # We assume that all passengers are unique and do not repeat
    different_passengers = total_passengers

    result = different_passengers
    return result

print(solution())