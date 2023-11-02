def solution():
    # Calculate the weight of leaves falling on Bill's roof every day
    weight_per_day = 100 * (1000/100)  # 1000 leaves weighs 1 pound

    # Calculate the number of days until Bill's roof collapses
    days_until_collapse = 500 / weight_per_day

    result = days_until_collapse
    return result

print(solution())