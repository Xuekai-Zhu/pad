def solution():
    """Jared wants to watch a series with four episodes. The first three episodes are 58 minutes, 62 minutes, and 65 minutes long respectively. If the four episodes last 4 hours, how long is the fourth episode?"""
    total_time = 4*60  # convert 4 hours to minutes
    first_three_time = 58 + 62 + 65
    fourth_time = total_time - first_three_time
    result = fourth_time
    return result

print(solution())