def solution():
     cost_of_charms = 15
     number_of_charms_per_necklace = 10
     sale_price_per_necklace = 200
     number_of_necklaces_sold = 30
     total_charm_cost = cost_of_charms * number_of_charms_per_necklace * number_of_necklaces_sold
     total_sale_price = sale_price_per_necklace * number_of_necklaces_sold
     profit = total_sale_price - total_charm_cost
     result = profit
     return result

print(solution())