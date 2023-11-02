def solution():
    # Total duration of the first three episodes
    total_duration = 58 + 62 + 65  # minutes

    # Convert total duration to hours
    total_duration = total_duration / 60  # hours

    # Duration of the fourth episode
    fourth_duration = 4 - total_duration  # 4 hours total, minus duration of first three episodes

    result = fourth_duration
    return result

print(solution())