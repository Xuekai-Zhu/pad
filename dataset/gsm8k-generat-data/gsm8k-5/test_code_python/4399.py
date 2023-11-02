def solution():
    total_budget = 60  # Lily has $60 to spend
    celery_price = 5  # The stalk of celery costs $5
    cereal_price = 12 * 0.5  # The cereal is 50% off and costs $6
    bread_price = 8  # The bread costs $8
    milk_price = 10 * 0.9  # The milk is 10% off and costs $9
    potatoes_price = 1 * 6  # Lily buys 6 potatoes and pays $1 for each
    total_spent = celery_price + cereal_price + bread_price + milk_price + potatoes_price  # Lily spends this much money
    coffee_budget = total_budget - total_spent # Lily has this much money left to spend on coffee
    result = coffee_budget
    return result

print(solution())