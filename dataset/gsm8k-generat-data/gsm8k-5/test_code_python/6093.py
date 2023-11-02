def solution():
    starting_squats = 30  # I started with 30 squats
    daily_increase = 5  # I increase the number of squats by 5 each day
    day_after_tomorrow = 3  # I want to know how many squats I will do the day after tomorrow (Day 3)

    # Calculate the total number of squats I will do in Day 3
    squats_day_three = starting_squats + (daily_increase * (day_after_tomorrow - 1))

    result = squats_day_three
    return result

print(solution())