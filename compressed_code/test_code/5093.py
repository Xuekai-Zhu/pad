def solution():
    
    seats_per_carriage = 25
    extra_seats_per_carriage = 10
    total_seats_per_carriage = seats_per_carriage + extra_seats_per_carriage
    carriages_per_train = 4
    passengers_per_train = total_seats_per_carriage * carriages_per_train
    trains = 3
    total_passengers = passengers_per_train * trains
    result = total_passengers
    return result

print(solution())