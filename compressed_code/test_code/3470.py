def solution():
    
    actor_cost = 1200
    food_cost = 50 * 3
    equipment_cost = 2 * (actor_cost + food_cost)
    total_cost = actor_cost + food_cost + equipment_cost
    revenue = 10000
    profit = revenue - total_cost
    result = profit
    return result

print(solution())