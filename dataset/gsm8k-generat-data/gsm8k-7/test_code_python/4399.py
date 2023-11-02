def solution():
    budget = 60

    # Calculate the cost of each item
    celery_cost = 5
    cereal_cost = 12 * 0.5
    bread_cost = 8
    milk_cost = 10 * 0.9
    potatoes_cost = 6 * 1

    # Calculate the total cost of all items
    total_cost = celery_cost + cereal_cost + bread_cost + milk_cost + potatoes_cost

    # Calculate the amount left over for coffee
    coffee_cost = budget - total_cost
    result = coffee_cost
    return result

print(solution())