def solution():
    # Calculate the total cost of actors, food, and equipment rental
    actor_cost = 1200
    food_cost = 50 * 3
    equipment_rental = 2 * (actor_cost + food_cost)
    total_cost = actor_cost + food_cost + equipment_rental

    # Calculate the total profit
    total_revenue = 10000
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())