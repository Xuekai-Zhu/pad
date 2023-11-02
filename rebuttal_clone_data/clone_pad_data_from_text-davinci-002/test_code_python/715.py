def solution():
     cost_of_strings = 1
     cost_of_beads = 3
     sale_price = 6
     bracelets_sold = 25
     total_cost = (cost_of_strings + cost_of_beads) * bracelets_sold
     total_profit = bracelets_sold * sale_price - total_cost
     result = total_profit
     return result

print(solution())