def solution():
    """Isabel loves to run in the forest and she does it within a circuit that is 365 meters long. She runs the circuit 7 times in the morning and runs it 3 times in the afternoon. How many meters does Isabel run during a week?"""
    # Define the length of the circuit and the number of times Isabel runs it in the morning and afternoon
    circuit_length = 365
    morning_runs = 7
    afternoon_runs = 3

    # Calculate the total distance Isabel runs in a week
    weekly_distance = (morning_runs + afternoon_runs) * circuit_length * 7

    # return the result
    result = weekly_distance
    return result

print(solution())