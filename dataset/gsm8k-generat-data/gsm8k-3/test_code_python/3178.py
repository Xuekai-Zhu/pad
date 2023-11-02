def solution():
    """Isabel does a 365-meter long circuit 7 times in the morning and 3 times in the afternoon. How many meters does she run during a week?"""
    # Define the length of the circuit
    CIRCUIT_LENGTH = 365

    # Calculate the total distance Isabel runs in a week
    morning_distance = 7 * CIRCUIT_LENGTH
    afternoon_distance = 3 * CIRCUIT_LENGTH
    total_distance = morning_distance + afternoon_distance

    # Display the total distance Isabel runs in a week
    result = total_distance
    return result

print(solution())