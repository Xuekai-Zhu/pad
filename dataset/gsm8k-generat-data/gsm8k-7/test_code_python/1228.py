def solution():
    # Number of drums made per day
    drums_per_day = 18 / 3  # 6 drums per day

    # Calculate the number of days to make 360 drums
    num_days = 360 / drums_per_day

    result = num_days
    return result

print(solution())