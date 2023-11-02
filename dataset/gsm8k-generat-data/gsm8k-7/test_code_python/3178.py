def solution():
    circuit_length = 365
    morning_runs = 7
    afternoon_runs = 3

    # Calculate the total distance Isabel runs in the morning
    morning_distance = circuit_length * morning_runs

    # Calculate the total distance Isabel runs in the afternoon
    afternoon_distance = circuit_length * afternoon_runs

    # Calculate the total distance Isabel runs in a week
    total_distance = morning_distance + afternoon_distance
    result = total_distance
    return result

print(solution())