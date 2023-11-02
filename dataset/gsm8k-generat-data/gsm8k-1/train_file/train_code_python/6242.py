def solution():
    """Jebb buys $50 worth of food at a restaurant with a service fee of 12%. After paying, he gives a $5 tip. How much money did he spend at the restaurant?"""
    food_cost = 50
    service_fee = food_cost * 0.12
    total_cost = food_cost + service_fee + 5
    result = total_cost
    return result

print(solution())