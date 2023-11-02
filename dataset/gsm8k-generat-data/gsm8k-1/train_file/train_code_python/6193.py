def solution():
    """Matt and Blake want to watch every episode of the show The Office. There are 201 episodes. If they watch 1 episode every Monday and 2 episodes every Wednesday each week, how many weeks will it take them to watch the whole series?"""
    total_episodes = 201
    episodes_per_week = 1+2
    weeks_to_finish = total_episodes/episodes_per_week
    result = weeks_to_finish
    return result

print(solution())