def solution():
    # Calculate how much money Sam makes per hour
    hourly_rate = 460 / 23  # Sam made $460 in 23 hours of yard work

    # Calculate how much Sam made from September to February
    money_from_shorter_period = hourly_rate * 8

    # Calculate Sam's total earnings
    total_earnings = 460 + money_from_shorter_period

    # Calculate how much Sam has left after fixing his car
    money_after_car_fix = total_earnings - 340

    # Calculate how much more Sam needs to save for the video game console
    remaining_money = 600 - money_after_car_fix

    # Calculate how many more hours Sam needs to work to make the remaining money
    required_hours = remaining_money / hourly_rate
    result = required_hours
    return result

print(solution())