def solution():
     bike_cost = 100
     allowance = 5
     extra_mowing = 10
     babysitting_hourly = 7
     money_saved = 65
     money_earned = allowance + extra_mowing + (babysitting_hourly * 2)
     money_needed = bike_cost - (money_saved + money_earned)
     result = money_needed
     return result

print(solution())