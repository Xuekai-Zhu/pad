def solution():
    
    total_budget = 60
    celery_price = 5
    cereal_price = 12 * 0.5
    bread_price = 8
    milk_price = 10 * 0.9
    potatoes_price = 1 * 6
    total_spent = celery_price + cereal_price + bread_price + milk_price + potatoes_price
    remaining_budget = total_budget - total_spent
    result = remaining_budget
    return result

print(solution())