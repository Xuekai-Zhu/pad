def solution():
    actor_cost = 1200
    food_cost = 50 * 3
    equipment_cost = (actor_cost + food_cost) * 2
    total_cost = actor_cost + food_cost + equipment_cost
    sale_price = 10000
    profit = sale_price - total_cost
    result = profit
    return result

print(solution())