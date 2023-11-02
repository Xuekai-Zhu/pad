def solution():
     chocolate_bars = 5
     bags_of_chips = 2
     total_cost = 20
     cost_of_chocolate_bars = chocolate_bars * 2
     cost_of_bags_of_chips = total_cost - cost_of_chocolate_bars
     price_per_bag_of_chips = cost_of_bags_of_chips / bags_of_chips
     result = price_per_bag_of_chips
     return result

print(solution())