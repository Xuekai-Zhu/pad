def solution():
    
    starting_logs = 6
    burned_logs = 3 * 3
    added_logs = 2 * 3
    remaining_logs = starting_logs + added_logs - burned_logs
    result = remaining_logs
    return result

print(solution())