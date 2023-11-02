def solution():
    tv_price = 1700
    hourly_wage = 10
    weekly_hours = 30
    total_hours_needed = tv_price / hourly_wage

    # Calculate the remaining hours needed to buy the TV
    remaining_hours = total_hours_needed - weekly_hours

    result = remaining_hours
    return result

print(solution())