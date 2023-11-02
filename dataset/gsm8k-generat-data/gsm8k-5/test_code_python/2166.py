def solution():
    turns_per_30_seconds = 6  # The wheel makes 6 turns every 30 seconds
    turns_per_hour = turns_per_30_seconds * 4  # There are 4 30-second intervals in one hour
    turns_in_two_hours = turns_per_hour * 2  # The machine runs for two hours

    result = turns_in_two_hours
    return result

print(solution())