def solution():
    """Jame's buys 100 head of cattle for $40,000. It cost 20% more than that to feed them. They each weigh 1000 pounds and sell for $2 per pound. How much profit did he make?"""
    cattle_cost = 40000
    feed_cost = cattle_cost * 1.2
    weight_per_cattle = 1000
    selling_price_per_pound = 2
    total_weight = weight_per_cattle * 100
    revenue = total_weight * selling_price_per_pound
    total_cost = cattle_cost + feed_cost
    profit = revenue - total_cost
    result = profit
    return result

print(solution())