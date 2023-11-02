def solution():
    starting_balance = 55  # Lily starts with $55 in her account
    shirt_cost = 7  # Lily spends $7 on a shirt
    other_shop_cost = shirt_cost * 3  # Lily spends three times as much as she spent on a shirt

    # Calculate the remaining balance
    remaining_balance = starting_balance - shirt_cost - other_shop_cost
    result = remaining_balance
    return result

print(solution())