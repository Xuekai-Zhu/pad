def solution():
    # Calculate the total amount of sodium in the original recipe
    salt_sodium = 2 * 50  # 2 teaspoons of salt, each with 50 mg of sodium
    cheese_sodium = 8 * 25  # 8 oz of parmesan cheese, each with 25 mg of sodium
    total_sodium = salt_sodium + cheese_sodium

    # Calculate the amount of sodium we need to reduce by
    sodium_reduction = total_sodium / 3

    # Calculate the amount of parmesan cheese we need to remove
    cheese_reduction = sodium_reduction / 25  # 25 mg of sodium per oz

    # Calculate the new amount of parmesan cheese needed
    new_cheese_amount = 8 - cheese_reduction

    result = new_cheese_amount
    return result

print(solution())