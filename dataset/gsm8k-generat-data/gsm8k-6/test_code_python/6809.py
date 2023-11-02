def solution():
    # Calculate the number of tasks completed by Jerry in one day
    tasks_per_day = 10 / 2  # each task takes 2 hours to complete

    # Calculate the amount earned by Jerry in one day
    earnings_per_day = tasks_per_day * 40

    # Calculate the total amount earned by Jerry in a week
    total_earnings = earnings_per_day * 7

    result = total_earnings
    return result

print(solution())