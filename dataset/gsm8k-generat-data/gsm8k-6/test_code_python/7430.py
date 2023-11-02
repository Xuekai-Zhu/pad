def solution():
    # Calculate the number of people currently sitting on the benches
    occupied_seats = 80

    # Calculate the maximum number of people the benches can accommodate
    max_capacity = 50 * 4

    # Calculate the number of available spaces on the benches
    available_seats = max_capacity - occupied_seats
    result = available_seats
    return result

print(solution())