def solution():
    tank_height = 18
    total_rainfall = 2 + (4 * 1) + (7 * 3)  # total rainfall in inches
    time_filled = (tank_height / total_rainfall) * 60  # time in minutes
    fill_hour = 1 + int(time_filled // 60)
    fill_minute = int(time_filled % 60)
    result = f"{fill_hour}:{fill_minute:02d} pm"
    return result

print(solution())