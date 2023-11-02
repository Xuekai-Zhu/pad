def solution():
    # Calculate the total distance Onur bikes in a week
    onur_weekly_distance = 5 * 250  

    # Calculate the total distance Hanil bikes in a week
    hanil_daily_distance = 250 + 40  # Hanil bikes 40 more kilometers than Onur
    hanil_weekly_distance = hanil_daily_distance * 5

    # Calculate the total distance both friends bike in a week
    total_distance = onur_weekly_distance + hanil_weekly_distance
    result = total_distance
    return result

print(solution())