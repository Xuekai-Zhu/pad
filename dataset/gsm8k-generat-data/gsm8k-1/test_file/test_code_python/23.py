def solution():
    """Cynthia eats one serving of ice cream every night. She buys cartons of ice cream with 15 servings of ice cream per carton at a cost of $4.00 per carton. After 60 days, how much will she spend on ice cream?"""
    servings_per_carton = 15
    cost_per_carton = 4
    days = 60
    servings_per_day = 1
    
    total_servings = servings_per_day * days
    total_cartons = total_servings / servings_per_carton
    total_cost = total_cartons * cost_per_carton
    result = total_cost
    
    return result

print(solution())