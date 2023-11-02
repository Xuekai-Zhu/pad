def solution():
    football_fields = 6
    yards_per_football_field = 200
    feet_per_minute = 400
    minutes_to_fetch_potato = (football_fields * yards_per_football_field) / feet_per_minute
    result = minutes_to_fetch_potato
    return result

print(solution())