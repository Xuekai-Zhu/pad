def solution():
    # Calculate the total number of days Randy has to practice before he turns 20
    total_days = (20 - 12) * 365 - 10   # subtracting 10 for the two weeks of vacation each year

    # Calculate the total number of practice hours Randy needs to reach 10,000 hours
    total_hours = 10000

    # Calculate the number of practice hours Randy needs per day
    hours_per_day = total_hours / total_days

    # Round up to the nearest integer since Randy cannot practice fractional hours
    hours_per_day = math.ceil(hours_per_day)

    result = hours_per_day
    return result

print(solution())