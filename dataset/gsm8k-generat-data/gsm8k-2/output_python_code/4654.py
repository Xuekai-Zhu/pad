def solution():
    """Adah practiced the cello for a total of 7.5 hours last week. He practiced for 86 minutes on each of 2 days. How many minutes in total did he practice on the other days?"""
    total_minutes = 7.5 * 60
    practiced_minutes = 86 * 2
    other_minutes = total_minutes - practiced_minutes
    result = other_minutes
    return result

print(solution())