def solution():
    
    original_speed = 65
    reduced_speed = original_speed - 20
    words_to_type = 810
    time_at_original_speed = words_to_type / original_speed
    time_at_reduced_speed = words_to_type / reduced_speed
    extra_time = time_at_reduced_speed - time_at_original_speed
    result = time_at_reduced_speed
    
    return result

print(solution())