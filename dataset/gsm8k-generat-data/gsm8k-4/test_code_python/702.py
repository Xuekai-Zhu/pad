def solution():
    """Lily had $55 in her account. She spent $7 on a shirt. She then went to another shop and spent thrice as much as she spent on a shirt. How much money is left in Lily's account?"""
    # Define the initial amount in Lily's account and the amount spent on a shirt
    initial_amount = 55
    shirt_cost = 7

    # Calculate the amount spent at the second shop
    second_shop_cost = shirt_cost * 3

    # Calculate the total amount spent
    total_spent = shirt_cost + second_shop_cost

    # Calculate the amount left in Lily's account
    amount_left = initial_amount - total_spent

    # return the result
    result = amount_left
    return result

print(solution())