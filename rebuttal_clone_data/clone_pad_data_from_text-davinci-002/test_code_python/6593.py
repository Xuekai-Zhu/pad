def solution():
     seats_per_carriage = 25
     carriages_per_train = 4
     extra_passengers_per_carriage = 10
     passengers_per_train = (seats_per_carriage + extra_passengers_per_carriage) * carriages_per_train
     trains = 3
     total_passengers = passengers_per_train * trains
     result = total_passengers
     return result

print(solution())