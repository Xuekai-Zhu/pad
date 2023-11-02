def solution():
    # Calculate the number of passengers on the bus at the last station
    current_passengers = 50 + 16 - 22 + 5*3  # 16 passengers get on at the first stop, 22 passengers get off at other stops, 5 more get on at other stops as well
    result = current_passengers
    return result

print(solution())