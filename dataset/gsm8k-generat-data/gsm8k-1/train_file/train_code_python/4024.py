def solution():
    """A vampire drains three people a week. His best friend is a werewolf who eats five people a week, but only fresh ones, never drained ones. How many weeks will a village of 72 people last them both?"""
    vampire_drain_rate = 3
    werewolf_eat_rate = 5
    village_population = 72
    total_people_consumed_per_week = vampire_drain_rate + werewolf_eat_rate
    weeks_until_deplete = village_population / total_people_consumed_per_week
    result = weeks_until_deplete
    return result

print(solution())