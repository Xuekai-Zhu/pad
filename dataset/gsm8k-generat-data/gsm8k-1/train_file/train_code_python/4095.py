def solution():
    """Mrs. Thompson bought 3 chickens for $3 each. She also bought a bag of potatoes. Mrs. Thompson paid $15 in total. How much did the potatoes cost?"""
    num_chickens = 3
    cost_per_chicken = 3
    total_chicken_cost = num_chickens * cost_per_chicken
    total_cost = 15
    potato_cost = total_cost - total_chicken_cost
    result = potato_cost
    return result

print(solution())