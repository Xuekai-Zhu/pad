def solution():
    """Isabel loves to run in the forest and she does it within a circuit that is 365 meters long. She runs the circuit 7 times in the morning and runs it 3 times in the afternoon. How many meters does Isabel run during a week?"""
    circuit_length = 365
    morning_runs = 7
    afternoon_runs = 3
    total_runs = morning_runs + afternoon_runs
    total_meters = total_runs * circuit_length
    result = total_meters
    return result

print(solution())