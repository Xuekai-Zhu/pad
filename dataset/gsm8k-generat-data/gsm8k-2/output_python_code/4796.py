def solution():
    """Zoe goes to the store to buy soda and pizza for herself and her 5 family members. Each bottle of soda costs half a dollar and each slice of pizza costs $1. Before she leaves her house she takes just enough money to pay for her purchase. How much money did Zoe take?"""
    num_people = 6
    soda_cost = 0.5
    pizza_cost = 1
    total_cost = (num_people * soda_cost) + (num_people * 2 * pizza_cost) # multiplies pizza by 2 since each person has 2 slices
    result = total_cost
    return result

print(solution())