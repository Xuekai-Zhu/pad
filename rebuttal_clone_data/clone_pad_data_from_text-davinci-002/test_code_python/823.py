def solution():
    initial_apples = 74
    apples_removed_by_ricki = 14
    apples_removed_by_samson = apples_removed_by_ricki * 2
    total_apples_removed = apples_removed_by_ricki + apples_removed_by_samson
    final_apple_count = initial_apples - total_apples_removed
    result = final_apple_count
    return result

print(solution())