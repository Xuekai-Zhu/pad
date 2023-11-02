def solution():
    
    typing_speed = 38
    total_words = 4560
    minutes_to_type = total_words / typing_speed
    hours_to_type = minutes_to_type / 60
    result = hours_to_type
    return result

print(solution())