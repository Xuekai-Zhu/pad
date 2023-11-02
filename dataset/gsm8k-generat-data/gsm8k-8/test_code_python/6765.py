def solution():
    # Define the initial number of frogs
    initial_frogs = 5

    # Add the number of frogs that climbed onto logs
    frogs_on_logs = 3
    total_frogs = initial_frogs + frogs_on_logs

    # Add the number of baby frogs on the rock
    baby_frogs_on_rock = 24
    total_frogs += baby_frogs_on_rock

    result = total_frogs
    return result

print(solution())