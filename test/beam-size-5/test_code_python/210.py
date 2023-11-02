def solution():
    # Calculate the amount of water in the big pool 4 minutes ago
    big_pool_4_minutes_ago = 2 * 4

    # Calculate the amount of water in the small pool 4 minutes ago
    small_pool_4_minutes_ago = big_pool_4_minutes_ago / 4

    # Calculate the amount of water in the small pool now
    small_pool_now = small_pool_4_minutes_ago / 4

    result = small_pool_now
    return result

print(solution())