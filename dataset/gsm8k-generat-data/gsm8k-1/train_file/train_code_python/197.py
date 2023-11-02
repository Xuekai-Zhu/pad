def solution():
    """Rosie runs 6 miles per hour. She runs for 1 hour on Monday, 30 minutes on Tuesday, 1 hour on Wednesday, and 20 minutes on Thursday. If she wants to run 20 miles for the week, how many minutes should she run on Friday?"""
    speed = 6  # in miles per hour
    time_monday = 1  # in hours
    time_tuesday = 0.5  # in hours
    time_wednesday = 1  # in hours
    time_thursday = 0.33  # in hours
    distance_covered = speed * (time_monday + time_tuesday + time_wednesday + time_thursday)
    distance_left = 20 - distance_covered  # in miles
    time_left = (distance_left / speed) * 60  # in minutes
    result = time_left
    return result

print(solution())