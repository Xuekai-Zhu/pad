def solution():
     cost_per_fish = 0.25
     sale_price_per_fish = 0.75
     new_tank_cost = 100
     percentage_short = 45
     percentage_needed = 100 - percentage_short
     goldfish_sold = math.ceil(percentage_needed / 100 * new_tank_cost / (sale_price_per_fish - cost_per_fish))
     result = goldfish_sold
     return result

print(solution())