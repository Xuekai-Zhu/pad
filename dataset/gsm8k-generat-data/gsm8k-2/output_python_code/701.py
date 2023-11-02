def solution():
    """Lily had $55 in her account. She spent $7 on a shirt. She then went to another shop and spent thrice as much as she spent on a shirt. How much money is left in Lily's account?"""
    starting_amount = 55
    shirt_cost = 7
    other_shop_cost = 3 * shirt_cost
    remaining_amount = starting_amount - shirt_cost - other_shop_cost
    result = remaining_amount
    return result

print(solution())