def solution():
    # Define the time it took James to heal before the skin graft
    initial_healing_time = 4

    # Define the percentage increase in time for healing from the skin graft
    skin_graft_increase = 0.5

    # Calculate the time it took James to heal from the skin graft
    skin_graft_time = initial_healing_time * (1 + skin_graft_increase)

    # Calculate the total time it took James to recover
    total_recovery_time = initial_healing_time + skin_graft_time

    result = total_recovery_time
    return result

print(solution())