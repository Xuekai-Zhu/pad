def solution():
    
    total_practice_time = 2 * 60
    piano_time = 30
    computer_time = 25
    history_time = 38
    used_time = piano_time + computer_time + history_time
    remaining_time = total_practice_time - used_time
    result = remaining_time
    return result

print(solution())