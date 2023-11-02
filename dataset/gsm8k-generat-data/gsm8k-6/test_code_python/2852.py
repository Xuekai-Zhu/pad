def solution():
    # Calculate the total amount of sodium in the original recipe
    sodium_salt = 2 * 50  # 2 teaspoons of salt, with 50mg of sodium per teaspoon
    sodium_parmesan = 8 * 25  # 8 oz of parmesan cheese, with 25mg of sodium per oz
    total_sodium = sodium_salt + sodium_parmesan

    # Calculate the amount of sodium to be reduced
    sodium_to_reduce = total_sodium / 3

    # Calculate the amount of parmesan cheese to be reduced by
    sodium_parmesan_per_oz = 25
    sodium_reduced_by_parmesan = sodium_to_reduce - sodium_salt
    ounces_parmesan_reduced = sodium_reduced_by_parmesan / sodium_parmesan_per_oz

    result = ounces_parmesan_reduced
    return result

print(solution())