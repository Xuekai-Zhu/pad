def solution():
    """James burned his hand in a freak accident. It takes him 4 weeks to heal enough to get a skin graft. After that, it takes him 50% longer than that to heal from the skin graft. How long did he take to recover from everything?"""
    initial_recovery_time = 4
    skin_graft_recovery_time = initial_recovery_time * 1.5
    total_recovery_time = initial_recovery_time + skin_graft_recovery_time
    result = total_recovery_time
    return result

print(solution())