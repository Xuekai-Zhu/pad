def solution():
    # Calculate the total cost of James' drinks
    drinks_cost = 6 * 6  # James buys 6 drinks for himself, each costing $6
    drinks_cost_with_tip = drinks_cost * 1.3  # James leaves a 30% tip on drinks
    # Calculate the total cost of James' food
    food_cost = 14
    food_cost_with_tip = food_cost * 1.3  # James leaves a 30% tip on food
    # Calculate the total cost of James' night out
    total_cost = 20 + drinks_cost_with_tip + food_cost_with_tip + (2 * 5 * 6 * 1.3)  # James buys 2 rounds for his 5 friends, with a 30% tip
    result = total_cost
    return result

print(solution())