def solution():
    # Calculate the total amount of rain for the week
    rain_total = 2 + 1 + 4 + 1 + 8  # Monday: 2 + 1, Tuesday: 2*2, Wednesday: 0, Thursday: 1, Friday: Monday to Thursday combined (2 + 1 + 4 + 1) = 8

    # Calculate the daily average rain total for the week
    daily_average = rain_total / 5  # total days in the week
    result = daily_average
    return result

print(solution())