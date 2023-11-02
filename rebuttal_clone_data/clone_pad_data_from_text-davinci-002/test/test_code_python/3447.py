def solution():
     candy_bars_bought = 20
     candy_bars_paid_for = 6
     cost_per_candy_bar = 1.50
     total_cost = candy_bars_bought * cost_per_candy_bar
     johns_cost = total_cost - (candy_bars_paid_for * cost_per_candy_bar)
     result = johns_cost
     return result

print(solution())