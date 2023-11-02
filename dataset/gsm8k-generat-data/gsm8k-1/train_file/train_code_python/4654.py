def solution():
    """Adah practiced the cello for a total of 7.5 hours last week. He practiced for 86 minutes on each of 2 days. How many minutes in total did he practice on the other days?"""
    total_practice_time = 7.5 * 60  # convert hours to minutes
    practice_time_2_days = 2 * 86
    practice_time_other_days = total_practice_time - practice_time_2_days
    result = practice_time_other_days
    return result

print(solution())