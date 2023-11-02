def solution():
    # Calculate the number of turns Barry can take standing on his head in 2 hours
    time_per_turn = 10 + 5  # 10 minutes standing + 5 minutes sitting = 15 minutes per turn
    total_time = 2 * 60  # 2 hours = 120 minutes
    max_turns = total_time // time_per_turn  # integer division
    result = max_turns
    return result

print(solution())