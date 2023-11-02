def solution():
    # Calculate the cost of actors
    actor_cost = 1200

    # Calculate the cost of food for 50 people
    food_cost = 50 * 3

    # Calculate the total cost of actors and food
    total_cost = actor_cost + food_cost

    # Calculate the equipment rental cost
    equipment_cost = 2 * total_cost

    # Calculate the total expenses
    total_expenses = total_cost + equipment_cost

    # Calculate the profit
    profit = 10000 - total_expenses
    result = profit

    return result

print(solution())