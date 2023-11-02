def solution():
    # Define the size of Jon's regular water bottle
    regular_size = 16

    # Calculate the amount of regular water Jon drinks in a day
    regular_daily_amount = (16 / 4) * 4

    # Calculate the size of Jon's larger water bottles
    larger_size = regular_size * 1.25

    # Calculate the amount of larger water Jon drinks in a day
    larger_daily_amount = (larger_size / 4) * 2

    # Calculate Jon's total daily fluid intake
    total_daily_amount = regular_daily_amount + larger_daily_amount

    # Calculate Jon's weekly fluid intake
    weekly_amount = total_daily_amount * 7
    result = weekly_amount
    return result

print(solution())