def solution():
    """Rosie runs 6 miles per hour. She runs for 1 hour on Monday, 30 minutes on Tuesday, 1 hour on Wednesday, and 20 minutes on Thursday. If she wants to run 20 miles for the week, how many minutes should she run on Friday?"""
    weekly_distance = 20
    distance_covered = 6 * 1 + 6 * 0.5 + 6 * 1 + 6 * 0.33 # running time multiplied by the speed
    remaining_distance = weekly_distance - distance_covered
    friday_time = (remaining_distance / 6) * 60 # convert to minutes
    result = friday_time
    return result

print(solution())