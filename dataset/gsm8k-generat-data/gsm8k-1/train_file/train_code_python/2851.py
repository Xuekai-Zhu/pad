def solution():
    """James is trying to avoid eating too much sodium. He's making a recipe that calls for 2 teaspoons of salt and 8 oz of parmesan cheese. Salt has 50 mg of sodium per teaspoon and parmesan has 25 mg of sodium per oz. If he can't reduce the salt, how many fewer ounces of parmesan cheese does he need to use to reduce the total amount of sodium by 1/3rd?"""
    salt_amount = 2 * 50  # 100 mg of sodium
    parmesan_amount = 8 * 25  # 200 mg of sodium
    total_sodium = salt_amount + parmesan_amount  # 300 mg of sodium

    reduced_sodium = total_sodium * (2/3)  # Reduce by 1/3rd
    reduced_parmesan = (reduced_sodium - salt_amount) / 25  # Find how much parmesan to reduce

    reduction = 8 - reduced_parmesan  # Find the difference in oz

    result = reduction
    return result

print(solution())