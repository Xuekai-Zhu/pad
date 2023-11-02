def solution():
    """James is trying to avoid eating too much sodium. He's making a recipe that calls for 2 teaspoons of salt and 8 oz of parmesan cheese. Salt has 50 mg of sodium per teaspoon and parmesan has 25 mg of sodium per oz. If he can't reduce the salt, how many fewer ounces of parmesan cheese does he need to use to reduce the total amount of sodium by 1/3rd?"""
    salt_sodium = 50 * 2
    parmesan_sodium = 25 * 8
    total_sodium = salt_sodium + parmesan_sodium
    target_sodium = total_sodium * (2/3)
    reduced_parma_sodium = target_sodium - salt_sodium
    reduced_parma_oz = reduced_parma_sodium / 25
    result = 8 - reduced_parma_oz
    return result

print(solution())