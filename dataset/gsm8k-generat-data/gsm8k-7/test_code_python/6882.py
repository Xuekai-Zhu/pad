def solution():
    weekly_pay = 5000/4  # Brendan is paid every week
    recharge_amount = weekly_pay / 2
    used_car_cost = 1500
    remaining_money = (5000 - used_car_cost) - (recharge_amount * 4)  # 4 weeks in June
    result = remaining_money
    return result

print(solution())