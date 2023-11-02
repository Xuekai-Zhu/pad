def solution():
    passengers_on = 200
    passengers_off = 320
    passengers_per_train = passengers_on + passengers_off
    trains_per_hour = 12
    total_passengers = passengers_per_train * trains_per_hour
    result = total_passengers
    return result

print(solution())