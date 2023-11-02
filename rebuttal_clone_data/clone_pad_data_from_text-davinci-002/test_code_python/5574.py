def solution():
    practice_hours_weekday = 3
    practice_hours_weekend = 5
    days_until_game = 21
    practice_hours_total = practice_hours_weekday * days_until_game + practice_hours_weekend * 2
    result = practice_hours_total
    return result

print(solution())