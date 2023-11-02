def solution():
    """Lily had $55 in her account. She spent $7 on a shirt. She then went to another shop and spent thrice as much as she spent on a shirt. How much money is left in Lily's account?"""
    initial_amount = 55
    shirt_cost = 7
    other_shop_cost = 3 * shirt_cost
    total_spent = shirt_cost + other_shop_cost
    money_left = initial_amount - total_spent
    result = money_left
    return result

print(solution())