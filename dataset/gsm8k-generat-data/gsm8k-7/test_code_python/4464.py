def solution():
    cost_actors = 1200
    num_people = 50
    cost_per_person = 3
    food_cost = num_people * cost_per_person

    equipment_cost = 2 * (cost_actors + food_cost)

    total_cost = cost_actors + food_cost + equipment_cost
    revenue = 10000

    profit = revenue - total_cost
    result = profit
    return result

print(solution())