def solution():
    # Calculate the total time James took to recover from everything
    time_to_heal = 4  # weeks to heal enough for a skin graft
    time_for_skin_graft = 1.5 * time_to_heal # 50% longer than healing enough for skin graft
    total_recovery_time = time_to_heal + time_for_skin_graft
    result = total_recovery_time
    return result

print(solution())