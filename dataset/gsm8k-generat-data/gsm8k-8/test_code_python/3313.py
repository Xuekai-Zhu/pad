def solution():
    # Define the amount of tea leaves used per day
    tea_per_day = 1/5

    # Define the amount of tea leaves in one box
    tea_per_box = 28

    # Calculate the number of days of tea per box
    days_per_box = tea_per_box / tea_per_day

    # Calculate the number of weeks of tea per box
    weeks_per_box = days_per_box / 7
    result = weeks_per_box
    return result

print(solution())