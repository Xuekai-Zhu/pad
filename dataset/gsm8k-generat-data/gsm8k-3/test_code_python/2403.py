def solution():
    """Five times a week, Onur bikes 250 kilometers a day. His friend Hanil bikes 40 more kilometers of Onur biking distance in a day. What's the total distance the two friends bikes in a week?"""
    # Define Onur's distance and Hanil's additional distance
    ONUR_DAILY_DIST = 250
    HANIL_ADDITIONAL_DIST = 40

    # Calculate Onur's weekly distance
    onur_weekly_dist = ONUR_DAILY_DIST * 5

    # Calculate Hanil's daily and weekly distance
    hanil_daily_dist = ONUR_DAILY_DIST + HANIL_ADDITIONAL_DIST
    hanil_weekly_dist = hanil_daily_dist * 5

    # Calculate the total distance the two friends biked in a week
    total_distance = onur_weekly_dist + hanil_weekly_dist

    # Display the total distance
    result = total_distance
    return result

print(solution())