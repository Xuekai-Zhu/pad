def solution():
    circuit_length = 365  # The circuit length is 365 meters
    morning_runs = 7  # Isabel runs the circuit 7 times in the morning
    afternoon_runs = 3  # Isabel runs the circuit 3 times in the afternoon
    days_per_week = 7  # There are 7 days in a week

    # Calculate the total distance Isabel runs in the morning
    morning_distance = circuit_length * morning_runs

    # Calculate the total distance Isabel runs in the afternoon
    afternoon_distance = circuit_length * afternoon_runs

    # Calculate the total distance Isabel runs in a week
    total_distance = (morning_distance + afternoon_distance) * days_per_week
    result = total_distance
    return result

print(solution())