def solution():
    
    bike_cost = 100
    saved_money = 65
    weekly_allowance = 5
    lawn_mowing_payment = 10
    babysitting_payment = 7 * 2
    total_money_earned = saved_money + weekly_allowance + lawn_mowing_payment + babysitting_payment
    money_left_to_save = bike_cost - total_money_earned
    result = money_left_to_save
    return result

print(solution())