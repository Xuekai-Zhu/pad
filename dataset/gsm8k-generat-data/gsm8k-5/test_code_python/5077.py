def solution():
    pages_left = 100 - 35 - (35-5)  # Pages left to read after 2 days
    pages_per_day = pages_left / 1  # Pages per day needed to finish in 3 days

    # Calculate the number of pages Lance needs to read tomorrow
    pages_tomorrow = pages_per_day - (35-5)

    result = pages_tomorrow
    return result

print(solution())