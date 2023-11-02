def solution():
    food_cost = 50  # Jebb spends $50 on food
    service_fee = 0.12 * food_cost  # Service fee is 12% of food cost
    total_cost = food_cost + service_fee + 5  # Jebb gives a $5 tip
    result = total_cost
    return result

print(solution())