def solution():
    """A wheel on a certain machine makes 6 turns every 30 seconds. How many turns does it make in two hours?"""
    turns_per_minute = 6 / 30
    turns_per_hour = turns_per_minute * 60
    total_turns = turns_per_hour * 2
    result = total_turns
    return result

print(solution())