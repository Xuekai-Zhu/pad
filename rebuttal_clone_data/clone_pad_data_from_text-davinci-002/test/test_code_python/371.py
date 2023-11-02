def solution():
     granola_cost = 3
     granola_sold = 15
     granola_discounted = 5
     price_per_bag = 6
     discounted_price = 4
     total_revenue = (granola_sold * price_per_bag) + (granola_discounted * discounted_price)
     total_cost = granola_cost * 20
     net_profit = total_revenue - total_cost
     result = net_profit
     return result

print(solution())