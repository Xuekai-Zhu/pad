def solution():
    total_time = 3 * 60  # The radio show plays for 3 hours, or 180 minutes
    talking_time = 3 * 10  # There are 3 talking segments, each lasting 10 minutes
    ad_time = 5 * 5  # There are 5 ad breaks, each lasting 5 minutes
    remaining_time = total_time - talking_time - ad_time  # Subtract the time for talking segments and ad breaks from total time

    # The remaining time is for songs, so that's our answer
    result = remaining_time
    return result

print(solution())