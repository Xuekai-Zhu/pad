def solution():
    # Calculate the number of days it would take Steven to plow his 55 acres of farmland
    plow_days = 55 // 10  # Steven can plow up to 10 acres per day

    # Calculate the number of days it would take Steven to mow his 30 acres of grassland
    mow_days = 30 // 12  # Steven can mow up to 12 acres per day

    # Calculate the total number of days it would take him to complete both tasks
    total_days = plow_days + mow_days
    result = total_days
    return result

print(solution())