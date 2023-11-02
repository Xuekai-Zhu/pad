def solution():
    minutes_for_breakfast = 20
    minutes_for_lunch = 5
    minutes_for_dinner = 10
    total_minutes = minutes_for_breakfast + minutes_for_lunch + (minutes_for_dinner * 4) + (30 * 3)
    result = total_minutes
    return result

print(solution())