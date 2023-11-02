def solution():
    yards_per_day_before = 8  # Brendan cuts 8 yards of grass per day before buying the lawnmower
    yards_per_day_after = yards_per_day_before * 1.5  # The lawnmower helps Brendan cut 50% more yards per day
    days_per_week = 7  # There are 7 days in a week

    # Calculate the total yards Brendan will cut in a week after buying the lawnmower
    total_yards_after = yards_per_day_after * days_per_week
    result = total_yards_after
    return result

print(solution())