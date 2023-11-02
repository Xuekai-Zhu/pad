def solution():
    """Lily had $55 in her account. She spent $7 on a shirt. She then went to another shop and spent thrice as much as she spent on a shirt. How much money is left in Lily's account?"""
    # Define the starting balance and cost of the shirt
    starting_balance = 55
    shirt_cost = 7

    # Calculate the remaining balance after buying the shirt
    balance_after_shirt = starting_balance - shirt_cost

    # Calculate how much Lily spent on the second shop
    second_shop_spending = 3 * shirt_cost

    # Calculate the remaining balance after the second shop
    remaining_balance = balance_after_shirt - second_shop_spending

    # Display the remaining balance
    result = remaining_balance
    return result

print(solution())