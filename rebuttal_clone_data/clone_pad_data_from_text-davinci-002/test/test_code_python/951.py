def solution():
     silver_ounces = 1.5
     silver_cost_per_ounce = 20
     total_silver_cost = silver_ounces * silver_cost_per_ounce
     gold_ounces = silver_ounces * 2
     gold_cost_per_ounce = silver_cost_per_ounce * 50
     total_gold_cost = gold_ounces * gold_cost_per_ounce
     total_cost = total_silver_cost + total_gold_cost
     result = total_cost
     return result

print(solution())