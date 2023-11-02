def solution():
    weeknight_hours = 2
    total_weekend_hours = 5
    practice_nights = 2
    homework_nights = 5 - practice_nights
    average_homework_hours = (weeknight_hours * homework_nights) / homework_nights
    result = average_homework_hours
    return result

print(solution())