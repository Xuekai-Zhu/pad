def solution():
    age_when_joined = 18
    time_to_become_chief = 8
    time_to_become_master_chief = 1.25 * time_to_become_chief  # 25% longer than the time to become chief
    time_in_service_before_retirement = 10
    total_time_in_service = time_to_become_chief + time_to_become_master_chief + time_in_service_before_retirement
    age_when_retired = age_when_joined + total_time_in_service
    result = age_when_retired
    return result

print(solution())