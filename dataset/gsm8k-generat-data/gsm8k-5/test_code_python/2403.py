def solution():
    onur_distance = 250  # Onur bikes 250 km a day
    hanil_distance = onur_distance + 40  # Hanil bikes 40 km more than Onur in a day
    days_per_week = 5  # The friends bike five times a week

    # Calculate the total distance Onur bikes in a week
    onur_weekly_distance = onur_distance * days_per_week

    # Calculate the total distance Hanil bikes in a week
    hanil_weekly_distance = hanil_distance * days_per_week

    # Calculate the total distance the two friends bike in a week
    total_weekly_distance = onur_weekly_distance + hanil_weekly_distance
    result = total_weekly_distance
    return result

print(solution())