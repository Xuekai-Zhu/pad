def solution():
    """James burned his hand in a freak accident.  It takes him 4 weeks to heal enough to get a skin graft.  After that it takes him 50% longer than that to heal from the skin graft.  How long did he take to recover from everything?"""
    # Define the time it takes James to heal before getting a skin graft and the time it takes to heal from the skin graft
    HEAL_TIME_BEFORE_SKIN_GRAFT = 4
    HEAL_TIME_AFTER_SKIN_GRAFT_MULTIPLIER = 1.5

    # Calculate the time it takes James to heal from the skin graft
    heal_time_after_skin_graft = HEAL_TIME_BEFORE_SKIN_GRAFT * HEAL_TIME_AFTER_SKIN_GRAFT_MULTIPLIER

    # Calculate the total time it takes James to recover from everything
    total_recovery_time = HEAL_TIME_BEFORE_SKIN_GRAFT + heal_time_after_skin_graft

    # Display the total recovery time
    result = total_recovery_time
    return result

print(solution())