def solution():
    
    actor_cost = 1200
    num_people = 50
    food_cost = num_people * 3
    equipment_rental_cost = (food_cost + actor_cost) * 2
    total_cost = actor_cost + food_cost + equipment_rental_cost
    sale_price = 10000
    profit = sale_price - total_cost
    result = profit
    return result

print(solution())