def solution():
    """Jame's buys 100 head of cattle for $40,000. It cost 20% more than that to feed them. They each weigh 1000 pounds and sell for $2 per pound. How much profit did he make?"""
    cattle_cost = 40000
    feeding_cost = 1.2 * cattle_cost
    total_cost = cattle_cost + feeding_cost
    total_weight = 100 * 1000
    price_per_pound = 2
    total_income = total_weight * price_per_pound
    profit = total_income - total_cost
    result = profit
    return result

print(solution())