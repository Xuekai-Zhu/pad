def solution():
    # Calculate the number of seats per carriage after accommodating 10 more passengers
    seats_per_carriage = 25 + 10

    # Calculate the total number of passengers per train
    passengers_per_train = seats_per_carriage * 4

    # Calculate the total number of passengers for 3 trains
    passengers_for_3_trains = passengers_per_train * 3
    result = passengers_for_3_trains
    return result

print(solution())