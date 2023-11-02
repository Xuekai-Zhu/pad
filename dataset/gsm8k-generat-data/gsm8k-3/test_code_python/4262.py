def solution():
    """Barry and his friend, Jim, went horseback riding across central Texas. They traveled at 5 miles per hour for 7 hours, and then stopped for the evening.  The next day, they traveled at 6 miles per hour for 6 hours, and then at half that speed for another three hours, before stopping to rest for the night.  On the third and final day, they traveled for 5 hours at 7 miles per hour.  In total, how far did they travel, in miles, during their horseback riding trip?"""
    # Calculate the distance traveled on the first day
    day1_distance = 5 * 7

    # Calculate the distance traveled on the second day
    day2_distance = 6 * 6 + 3 * 3

    # Calculate the distance traveled on the third day
    day3_distance = 7 * 5

    # Calculate the total distance traveled
    total_distance = day1_distance + day2_distance + day3_distance

    # Display the total distance traveled
    result = total_distance
    return result

print(solution())