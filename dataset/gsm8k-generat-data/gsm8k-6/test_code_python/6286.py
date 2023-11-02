def solution():
    # Calculate the number of bees in the hive after 7 days
    starting_bees = 12500  # number of bees at the start
    daily_gain = 3000 - 900  # number of bees gained per day (hatching minus loss)
    total_gain = daily_gain * 7  # total number of bees gained after 7 days
    total_bees = starting_bees + total_gain  # total number of bees after 7 days
    result = total_bees
    return result

print(solution())