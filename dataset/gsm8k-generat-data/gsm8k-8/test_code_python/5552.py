def solution():
    # Calculate the total duration of the first three episodes
    total_duration = 58 + 62 + 65

    # Calculate the remaining duration for the fourth episode
    remaining_duration = (4 * 60) - total_duration

    result = remaining_duration
    return result

print(solution())