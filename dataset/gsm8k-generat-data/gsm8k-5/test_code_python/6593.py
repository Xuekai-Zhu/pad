def solution():
    seats_per_carriage = 25  # Each carriage has 25 seats
    extra_seats_per_carriage = 10  # Each carriage can accommodate 10 more passengers
    total_seats_per_carriage = seats_per_carriage + extra_seats_per_carriage  # Total seats per carriage after accommodating more passengers
    carriages_per_train = 4  # There are 4 carriages in each train
    passengers_per_train = total_seats_per_carriage * carriages_per_train  # Total number of passengers in each train
    trains = 3  # We want to know the total number of passengers in 3 trains

    # Calculate the total number of passengers in 3 trains
    total_passengers = passengers_per_train * trains
    result = total_passengers
    return result

print(solution())