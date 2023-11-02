def solution():
    cost_per_bag = 3.0
    selling_price = 6.0
    discounted_price = 4.0
    num_bags = 20
    num_bags_sold = 15
    num_discounted_bags_sold = 5
    
    # Calculate the total cost of all bags of granola
    total_cost = cost_per_bag * num_bags
    
    # Calculate the total revenue from bags sold at full price
    full_price_revenue = num_bags_sold * selling_price
    
    # Calculate the total revenue from discounted bags
    discounted_revenue = num_discounted_bags_sold * discounted_price
    
    # Calculate the total revenue
    total_revenue = full_price_revenue + discounted_revenue
    
    # Calculate the net profit
    net_profit = total_revenue - total_cost
    
    result = net_profit
    return result

print(solution())