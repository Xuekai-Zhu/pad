def solution():
    chocolates_per_week = 3  # 2 for herself and 1 for sister
    extra_chocolates = 10  # for Charlie's birthday
    num_weeks = 4

    # Calculate the total number of chocolates Kantana bought for herself and sister
    total_regular_chocolates = chocolates_per_week * num_weeks

    # Calculate the total number of chocolates including the birthday gift
    total_chocolates = total_regular_chocolates + extra_chocolates
    result = total_chocolates
    return result

print(solution())