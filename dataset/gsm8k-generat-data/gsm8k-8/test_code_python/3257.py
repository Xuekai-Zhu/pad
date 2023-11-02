def solution():
    # Define the initial number of passengers
    num_passengers = 50

    # Add the 16 passengers who got on at the first stop
    num_passengers += 16

    # Subtract the 22 passengers who got off at the next stops
    num_passengers -= 22

    # Add the 5 passengers who got on at the subsequent stops
    num_passengers += 5

    result = num_passengers
    return result

print(solution())