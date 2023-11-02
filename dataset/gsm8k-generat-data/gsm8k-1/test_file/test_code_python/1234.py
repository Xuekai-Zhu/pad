def solution():
    """Bud makes homemade macaroni and cheese once a week. The pasta costs $1.00 a box, and he spends $3.00 on cheddar cheese and twice that amount for the gruyere cheese. How much money does Bud spend on making macaroni and cheese in one year?"""
    pasta_cost = 1.00
    cheddar_cost = 3.00
    gruyere_cost = 2 * cheddar_cost
    total_cost = pasta_cost + cheddar_cost + gruyere_cost
    weeks_in_year = 52
    total_cost_yearly = total_cost * weeks_in_year
    result = total_cost_yearly
    return result

print(solution())