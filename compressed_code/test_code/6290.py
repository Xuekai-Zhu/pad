def solution():
    
    cost_per_bag = 3
    selling_price_full = 6
    selling_price_discount = 4
    total_bags = 20
    bags_sold_full = 15
    bags_sold_discount = 5
    
    revenue_full = bags_sold_full * selling_price_full
    revenue_discount = bags_sold_discount * selling_price_discount
    total_revenue = revenue_full + revenue_discount
    profit = total_revenue - (total_bags * cost_per_bag)
    result = profit
    
    return result

print(solution())