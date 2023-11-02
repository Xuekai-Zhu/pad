def solution():
    
    initial_passengers = 50
    passengers_first_stop = initial_passengers - 15
    passengers_second_stop = passengers_first_stop - 8 + 2
    passengers_third_stop = passengers_second_stop - 4 + 3
    result = passengers_third_stop
    return result

print(solution())