def solution():
    starting_squats = 30
    daily_increase = 5
    squats_day2 = starting_squats + daily_increase  # number of squats on day 2
    squats_day3 = squats_day2 + daily_increase  # number of squats on day 3 (the day after tomorrow)
    result = squats_day3
    return result

print(solution())