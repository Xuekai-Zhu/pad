def solution():
    
    words_per_page = 400
    total_words = words_per_page * 5
    typing_speed = 50
    typing_time = total_words / typing_speed
    water_per_hour = 15
    water_needed = (typing_time / 60) * water_per_hour
    result = water_needed
    return result

print(solution())