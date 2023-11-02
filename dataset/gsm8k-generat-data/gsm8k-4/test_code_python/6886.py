def solution():
    """A baseball cap factory made 320 caps the first week, 400 the second week, and 300 the third week. If the company makes their average number of caps from the first 3 weeks during the fourth week, how many total caps will they make?"""
    # Define the caps made in each week
    caps_week1 = 320
    caps_week2 = 400
    caps_week3 = 300

    # Calculate the total caps made in the first 3 weeks
    total_caps = caps_week1 + caps_week2 + caps_week3

    # Calculate the average caps made per week in the first 3 weeks
    avg_caps_per_week = total_caps / 3

    # Calculate the predicted caps made in the fourth week
    caps_week4 = int(avg_caps_per_week)

    # Calculate the total caps made in all 4 weeks
    total_caps_made = total_caps + caps_week4

    # Return the result
    result = total_caps_made
    return result

print(solution())