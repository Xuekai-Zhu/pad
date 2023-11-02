def solution():
    """James buys a weight vest for $250. He then buys 200 pounds of weight plates for $1.2 per pound. A 200-pound weight vest would cost $700 but there is a $100 discount. How much does he save with his vest?"""
    vest_cost = 250
    plate_cost_per_pound = 1.2
    plate_weight = 200
    regular_weight_vest_cost = 700
    discount = 100

    total_cost = vest_cost + (plate_cost_per_pound * plate_weight)
    regular_cost = regular_weight_vest_cost - discount

    savings = regular_cost - total_cost
    result = savings
    return result

print(solution())