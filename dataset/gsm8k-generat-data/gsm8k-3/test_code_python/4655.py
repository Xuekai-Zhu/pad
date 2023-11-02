def solution():
    """Adah practiced the cello for a total of 7.5 hours last week. He practiced for 86 minutes on each of 2 days. How many minutes in total did he practice on the other days?"""
    # Calculate the total practice time in minutes
    total_practice_time = 7.5 * 60

    # Calculate the practice time on the two days
    practice_time_on_2_days = 2 * 86

    # Calculate the practice time on the other days
    practice_time_on_other_days = total_practice_time - practice_time_on_2_days

    # Display the practice time on the other days
    result = practice_time_on_other_days
    return result

print(solution())