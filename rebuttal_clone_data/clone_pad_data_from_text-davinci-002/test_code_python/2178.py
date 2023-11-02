def solution():
     initial_cost = 100
     six_month_loss = initial_cost * 0.25
     one_year_loss = initial_cost * 0.2
     Lawnmower_value = initial_cost - six_month_loss - one_year_loss
     result = Lawnmower_value
     return result

print(solution())