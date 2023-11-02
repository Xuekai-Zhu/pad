def solution():
    """Jamal bought 4 half dozen colored crayons at $2 per crayon. What was the total cost of the crayons that she bought?"""
    crayons_per_half_dozen = 6
    half_dozen_bought = 4
    price_per_crayon = 2
    total_crayons = crayons_per_half_dozen * half_dozen_bought
    total_cost = total_crayons * price_per_crayon
    result = total_cost
    return result

print(solution())