def solution():
    initial_passengers = 50
    passengers_on = 16
    passengers_off = 22
    passengers_on_2 = 5
    total_passengers = initial_passengers + passengers_on - passengers_off + passengers_on_2
    result = total_passengers
    return result

print(solution())