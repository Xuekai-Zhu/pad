def solution():
    # Calculate the total amount of sodium in the original recipe
    sodium_salt = 2 * 50  # 2 teaspoons of salt, with 50 mg of sodium per teaspoon
    sodium_parmesan = 8 * 25  # 8 oz of parmesan cheese, with 25 mg of sodium per oz
    total_sodium = sodium_salt + sodium_parmesan

    # Calculate the amount of sodium James needs to reduce in order to cut it by 1/3
    sodium_to_reduce = total_sodium / 3 

    # Calculate how much less parmesan cheese James needs to use to reduce the sodium by 1/3
    sodium_in_one_oz = 25  # 1 oz of parmesan cheese has 25 mg of sodium
    oz_to_reduce = sodium_to_reduce / sodium_in_one_oz

    result = oz_to_reduce
    return result

print(solution())