def solution():
    time_to_heal = 4 * 7  # 4 weeks to heal

    time_for_skin_graft = 1.5 * time_to_heal  # 50% longer than time to heal

    total_recovery_time = time_to_heal + time_for_skin_graft
    result = total_recovery_time
    return result

print(solution())