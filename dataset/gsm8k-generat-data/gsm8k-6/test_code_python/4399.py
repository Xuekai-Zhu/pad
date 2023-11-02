def solution():
    # Calculate the total cost of the items Lily plans to buy
    celery_cost = 5
    cereal_cost = 0.5 * 12
    bread_cost = 8
    milk_cost = 10 * 0.9
    potatoes_cost = 6 * 1
    total_cost = celery_cost + cereal_cost + bread_cost + milk_cost + potatoes_cost

    # Calculate the amount of money Lily has left after buying the other items
    money_left = 60 - total_cost
    result = money_left
    return result

print(solution())