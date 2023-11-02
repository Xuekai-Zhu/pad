def solution():
    """James is trying to avoid eating too much sodium. He's making a recipe that calls for 2 teaspoons of salt and 8 oz of parmesan cheese. Salt has 50 mg of sodium per teaspoon and parmesan has 25 mg of sodium per oz. If he can't reduce the salt, how many fewer ounces of parmesan cheese does he need to use to reduce the total amount of sodium by 1/3rd?"""
    # Define the sodium content of salt and parmesan
    SALT_SODIUM = 50  # mg per teaspoon
    PARMESAN_SODIUM = 25  # mg per oz

    # Define the amount of salt and parmesan in the recipe
    salt_amount = 2  # teaspoons
    parmesan_amount = 8  # oz

    # Calculate the total sodium content of the recipe
    total_sodium = (salt_amount * SALT_SODIUM) + (parmesan_amount * PARMESAN_SODIUM)

    # Calculate the amount of sodium James wants to reduce by
    sodium_reduction = total_sodium / 3

    # Calculate how many ounces of parmesan James needs to use less of to reduce sodium content
    parmesan_reduction = sodium_reduction / PARMESAN_SODIUM

    # Calculate the new amount of parmesan James should use
    new_parmesan_amount = parmesan_amount - parmesan_reduction

    # Display the amount of parmesan James needs to use less of
    result = parmesan_amount - new_parmesan_amount
    return result

print(solution())