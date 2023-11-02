def solution():
    healing_time_before_graft = 4  # James takes 4 weeks to heal enough for skin graft
    healing_time_after_graft = healing_time_before_graft * 1.5  # It takes him 50% longer to heal from skin graft
    total_healing_time = healing_time_before_graft + healing_time_after_graft  # Total time to recover

    result = total_healing_time
    return result

print(solution())