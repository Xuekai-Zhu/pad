def solution():
    total_questions = 60
    multiple_choice = 30
    fill_in_the_blank = 30
    minutes_per_multiple_choice = 15
    minutes_per_fill_in_the_blank = 25
    total_minutes = (multiple_choice * minutes_per_multiple_choice) + (fill_in_the_blank * minutes_per_fill_in_the_blank)
    total_hours = total_minutes / 60
    result = total_hours
    return result

print(solution())