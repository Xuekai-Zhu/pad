def solution():
    """James is trying to avoid eating too much sodium. He's making a recipe that calls for 2 teaspoons of salt and 8 oz of parmesan cheese. Salt has 50 mg of sodium per teaspoon and parmesan has 25 mg of sodium per oz. If he can't reduce the salt, how many fewer ounces of parmesan cheese does he need to use to reduce the total amount of sodium by 1/3rd?"""
    # Define the amount of salt and parmesan cheese in the recipe
    salt_amount = 2 * 50 # 50 mg of sodium per teaspoon
    parmesan_amount = 8 * 25 # 25 mg of sodium per oz

    # Calculate the total amount of sodium in the recipe
    total_sodium = salt_amount + parmesan_amount

    # Calculate the amount of sodium James wants to reduce by
    sodium_reduction = total_sodium / 3

    # Calculate the amount of parmesan cheese James needs to use to achieve the desired sodium reduction
    parmesan_reduction = sodium_reduction / 25 # 25 mg of sodium per oz

    # Subtract the parmesan reduction from the initial parmesan amount to get the final amount of parmesan needed
    final_parmesan_amount = 8 - parmesan_reduction

    # Calculate the difference in parmesan amount
    parmesan_difference = 8 - final_parmesan_amount
    
    result = parmesan_difference
    return result

print(solution())