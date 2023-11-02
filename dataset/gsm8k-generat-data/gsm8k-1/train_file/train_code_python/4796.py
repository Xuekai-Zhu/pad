def solution():
    """Zoe goes to the store to buy soda and pizza for herself and her 5 family members. Each bottle of soda costs half a dollar and each slice of pizza costs $1. Before she leaves her house she takes just enough money to pay for her purchase. How much money did Zoe take?"""
    soda_cost = 0.5
    pizza_cost = 1
    num_family_members = 5
    total_cost = (soda_cost * (num_family_members + 1)) + (pizza_cost * (num_family_members + 1))
    money_taken = total_cost
    result = money_taken
    return result

print(solution())