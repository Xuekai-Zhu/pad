def solution():
    
    audiobook_length = 30
    daily_listening_time = 2
    total_listening_time = audiobook_length * 6
    days_to_finish = total_listening_time / daily_listening_time
    result = days_to_finish
    return result

print(solution())