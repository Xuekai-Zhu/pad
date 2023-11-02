def solution():
    """Violetta wants to buy new crayons. She needs them in 5 different colors and prepared $20 for this purchase. One crayon costs $2. How much change will she get?"""
    num_colors = 5
    cost_per_crayon = 2
    total_cost = num_colors * cost_per_crayon
    money_paid = 20
    change = money_paid - total_cost
    result = change
    return result

print(solution())