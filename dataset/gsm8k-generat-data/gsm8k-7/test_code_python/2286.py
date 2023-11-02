def solution():
    total_money_collected = 240
    hourly_wage = 10
    tip_money = 50

    # Subtract tip money from total money collected to get total earned through hourly wage
    hourly_money = total_money_collected - tip_money

    # Divide hourly money by hourly wage to get total hours worked
    total_hours = hourly_money / hourly_wage
    result = total_hours
    return result

print(solution())