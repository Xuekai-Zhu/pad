def solution():
    """James burned his hand in a freak accident. It takes him 4 weeks to heal enough to get a skin graft. After that it takes him 50% longer than that to heal from the skin graft. How long did he take to recover from everything?"""
    # Define the time it takes James to heal before the skin graft
    phase_1 = 4

    # Calculate the extra time it takes to heal after the skin graft
    phase_2 = 1.5 * phase_1

    # Calculate the total time it takes James to recover
    total_recovery_time = phase_1 + phase_2

    # Return the result
    result = total_recovery_time
    return result

print(solution())