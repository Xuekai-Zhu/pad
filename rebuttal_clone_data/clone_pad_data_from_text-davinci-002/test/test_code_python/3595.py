def solution():
     total_teeth = 20
     total_money = 54
     lost_teeth = total_teeth - 2
     money_first_tooth = 20
     money_per_tooth = (total_money - money_first_tooth) / lost_teeth
     result = money_per_tooth
     return result

print(solution())