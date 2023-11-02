def solution():
    # Calculate the total hours Doris can babysit in a week
    weekly_hours = 3 * 5 + 5

    # Calculate Doris' weekly earnings
    weekly_earnings = weekly_hours * 20

    # Calculate the number of weeks needed to earn at least $1200
    weeks_needed = 1200 // weekly_earnings
    if 1200 % weekly_earnings > 0:
        weeks_needed += 1

    result = weeks_needed
    return result

print(solution())