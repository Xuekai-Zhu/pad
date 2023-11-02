def solution():
    apples_per_day = 4  # Adam picks 4 apples per day
    days = 30  # Adam picks apples for 30 days

    # Calculate the total number of apples picked in 30 days
    total_apples_picked = apples_per_day * days

    # Add the remaining apples to the total
    total_apples = total_apples_picked + 230
    result = total_apples
    return result

print(solution())