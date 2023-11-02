def solution():
    first_day_pills = 1
    pills_increase_per_day = 2
    days_per_week = 7

    # Calculate the total number of pills Joey will take in a week
    total_pills = 0
    for i in range(days_per_week):
        total_pills += first_day_pills + (pills_increase_per_day * i)

    result = total_pills
    return result

print(solution())