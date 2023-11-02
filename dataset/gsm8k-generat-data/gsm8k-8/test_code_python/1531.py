def solution():
    # Calculate total time for preparing for mountain climbing
    total_prep_time = 2 + 2*2  # 2 years to get in shape and 2*2 years to learn climbing skills

    # Calculate total time to climb all seven summits
    total_climbing_time = 7 * 5  # 5 months to climb each summit

    # Calculate total time for cave diving
    total_diving_time = 13 + 2  # 13 months of learning and 2 years of diving

    # Calculate total time for all goals
    total_time = total_prep_time + total_climbing_time + total_diving_time
    result = total_time
    return result

print(solution())