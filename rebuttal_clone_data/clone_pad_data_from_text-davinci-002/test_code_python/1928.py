def solution():
    initial_passengers = 100
    return_passengers = 60
    total_passengers = initial_passengers + return_passengers + (initial_passengers * 3)
    result = total_passengers
    return result

print(solution())