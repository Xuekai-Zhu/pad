def solution():
    original_speed = 212
    reduced_speed = original_speed - 40
    total_words = 3440
    time_with_left_hand = total_words / original_speed
    time_without_left_hand = total_words / reduced_speed
    additional_time = time_with_left_hand - time_without_left_hand
    result = round(additional_time * 60)
    return result

print(solution())