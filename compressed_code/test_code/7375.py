def solution():
    
    words_per_page = 400
    pages_to_write = 5
    total_words = words_per_page * pages_to_write
    typing_time_minutes = total_words / 50
    typing_time_hours = typing_time_minutes / 60
    water_per_hour = 15
    water_to_drink = typing_time_hours * water_per_hour
    result = water_to_drink
    return result

print(solution())