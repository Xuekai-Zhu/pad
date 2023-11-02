def solution():
    total_pipe_length = 40  # Edward needs 40 feet of copper pipe
    bolts_needed = total_pipe_length // 5  # For every 5 feet of pipe, one tightening bolt is needed
    washers_needed = 2 * bolts_needed  # Two washers are needed for every tightening bolt

    # Calculate the remaining washers after the job is done
    remaining_washers = 20 - washers_needed
    result = remaining_washers
    return result

print(solution())