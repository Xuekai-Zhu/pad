def solution():
    regular_pay = 80  # John makes $80 a day without the bonus
    bonus_pay = 100  # John makes $100 a day with the bonus
    regular_hours = 8  # John works 8 hours a day without the bonus
    bonus_hours = 10  # John works 10 hours a day with the bonus
    bonus_time = 2  # John works 2 extra hours a day to earn the bonus

    # Calculate John's hourly rate without the bonus
    regular_rate = regular_pay / regular_hours

    # Calculate John's hourly rate with the bonus
    bonus_rate = bonus_pay / bonus_hours

    # If John chooses to earn the bonus, calculate his new hourly rate
    if bonus_rate > regular_rate:
      hours_worked = regular_hours + bonus_time
      hourly_rate = bonus_pay / hours_worked
    else:
      hourly_rate = regular_rate

    result = hourly_rate
    return result

print(solution())