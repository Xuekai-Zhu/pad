def solution():
    """A vampire drains three people a week. His best friend is a werewolf who eats five people a week, but only fresh ones, never drained ones. How many weeks will a village of 72 people last them both?"""
    vampire_drains = 3
    werewolf_eats = 5
    total_people = 72
    weeks = total_people / (vampire_drains + werewolf_eats)
    result = weeks
    return result

print(solution())