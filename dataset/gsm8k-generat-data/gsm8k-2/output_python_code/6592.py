def solution():
    """There are 4 carriages in a train and each carriage has 25 seats. If each carriage could accommodate 10 more passengers, how many passengers would fill up 3 trains?"""
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