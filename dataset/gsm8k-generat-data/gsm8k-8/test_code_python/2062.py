def solution():
    total_time = 2 * 60
    piano_time = 30
    computer_time = 25
    history_time = 38

    # Calculate total time spent
    total_spent_time = piano_time + computer_time + history_time

    # Calculate the remaining time for finger exercise
    remaining_time = total_time - total_spent_time
    result = remaining_time
    return result

print(solution())