def solution():
    """Adah practiced the cello for a total of 7.5 hours last week. He practiced for 86 minutes on each of 2 days. How many minutes in total did he practice on the other days?"""
    # Define the total practice time in minutes
    total_practice_minutes = 7.5 * 60

    # Calculate the practice time on the two days
    two_day_practice = 86 * 2

    # Calculate the practice time on the other days
    other_day_practice = total_practice_minutes - two_day_practice

    result = other_day_practice
    return result

print(solution())