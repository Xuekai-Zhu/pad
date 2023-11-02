def solution():
    num_carriages = 4
    seats_per_carriage = 25
    extra_seats_per_carriage = 10
    num_trains = 3

    # Calculate the total number of seats in each carriage after accommodating extra passengers
    total_seats_per_carriage = seats_per_carriage + extra_seats_per_carriage

    # Calculate the total number of passengers that can be accommodated in each carriage
    total_passengers_per_carriage = total_seats_per_carriage

    # Calculate the total number of passengers that can fill up one train
    total_passengers_per_train = total_passengers_per_carriage * num_carriages

    # Calculate the total number of passengers that can fill up all trains
    total_passengers = total_passengers_per_train * num_trains
    result = total_passengers
    return result

print(solution())