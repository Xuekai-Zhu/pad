def solution():
    """A wheel on a certain machine makes 6 turns every 30 seconds. How many turns does it make in two hours?"""
    turns_per_30_seconds = 6
    seconds_per_hour = 3600 # 60 seconds per minute * 60 minutes per hour
    turns_per_hour = turns_per_30_seconds * (seconds_per_hour / 30)
    turns_in_two_hours = turns_per_hour * 2
    result = turns_in_two_hours
    return result

print(solution())