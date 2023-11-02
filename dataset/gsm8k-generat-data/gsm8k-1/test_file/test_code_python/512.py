def solution():
    """On average Joe throws 25 punches per minute. A fight lasts 5 rounds of 3 minutes. How many punches did he throw?"""
    punches_per_minute = 25
    rounds = 5
    minutes_per_round = 3
    total_punches = punches_per_minute * rounds * minutes_per_round
    result = total_punches
    return result

print(solution())