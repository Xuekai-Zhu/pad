def solution():
     ad_cost = 1000
     customers = 100
     percent_customers_buying = 80
     customers_buying = customers * (percent_customers_buying / 100)
     cost_per_item = 25
     total_revenue = customers_buying * cost_per_item
     profit = total_revenue - ad_cost
     result = profit
     return result

print(solution())