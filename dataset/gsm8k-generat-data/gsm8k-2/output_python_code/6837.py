def solution():
    """John went on a mission that was supposed to take 5 days. Instead it took 60% longer. He then had to go on a second mission which took 3 days. How long was he on missions?"""
    first_mission_days = 5
    first_mission_extra_days = 0.6 * first_mission_days
    total_first_mission_days = first_mission_days + first_mission_extra_days
    second_mission_days = 3
    total_mission_days = total_first_mission_days + second_mission_days
    result = total_mission_days
    return result

print(solution())