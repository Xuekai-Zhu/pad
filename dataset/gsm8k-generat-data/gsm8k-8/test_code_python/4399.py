def solution():
    total_budget = 60

    # Calculate the cost of each item
    celery_cost = 5
    cereal_cost = 0.5 * 12
    bread_cost = 8
    milk_cost = 0.9 * 10
    potatoes_cost = 6

    # Calculate the total cost of all items
    total_cost = celery_cost + cereal_cost + bread_cost + milk_cost + potatoes_cost

    # Calculate how much money Lily has left after buying all the items
    remaining_budget = total_budget - total_cost

    # Calculate how much Lily can spend on coffee
    coffee_budget = remaining_budget

    result = coffee_budget
    return result

print(solution())