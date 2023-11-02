def solution():
    """Tina buys a loaf of bread for $50, 2oz of ham for $150, and a cake for $200. What percent of the cost is the ham and bread?"""
    bread_cost = 50
    ham_cost = 150
    total_cost = bread_cost + ham_cost + 200
    combined_cost = bread_cost + ham_cost
    percent = (combined_cost/total_cost) * 100
    result = percent
    return result

print(solution())