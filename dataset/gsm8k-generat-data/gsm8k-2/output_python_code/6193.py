def solution():
    """Matt and Blake want to watch every episode of the show The Office. There are 201 episodes. If they watch 1 episode every Monday and 2 episodes every Wednesday each week, how many weeks will it take them to watch the whole series?"""
    total_episodes = 201
    monday_episodes = 1
    wednesday_episodes = 2
    total_weeks = 0
    while total_episodes > 0:
        total_episodes -= monday_episodes + wednesday_episodes * 2
        total_weeks += 1
    result = total_weeks
    return result

print(solution())