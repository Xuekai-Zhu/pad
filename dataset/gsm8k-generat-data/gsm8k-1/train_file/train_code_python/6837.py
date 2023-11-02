def solution():
    """John went on a mission that was supposed to take 5 days. Instead it took 60% longer. He then had to go on a second mission which took 3 days. How long was he on missions?"""
    initial_mission_duration = 5
    percent_increase = 60
    increased_duration = initial_mission_duration * (1 + (percent_increase / 100))
    total_duration = increased_duration + 3
    result = total_duration
    return result

print(solution())