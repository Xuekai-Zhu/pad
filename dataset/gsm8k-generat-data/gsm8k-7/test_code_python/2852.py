def solution():
    salt_teaspoons = 2
    salt_sodium_per_teaspoon = 50
    parmesan_oz = 8
    parmesan_sodium_per_oz = 25
    sodium_reduction = 1/3

    # Calculate the total amount of sodium in the original recipe
    total_sodium_original = (salt_teaspoons * salt_sodium_per_teaspoon) + (parmesan_oz * parmesan_sodium_per_oz)

    # Calculate the amount of sodium to be reduced
    sodium_reduction_amount = total_sodium_original * sodium_reduction

    # Calculate the amount of parmesan to be reduced to achieve the sodium reduction
    parmesan_reduction_oz = sodium_reduction_amount / parmesan_sodium_per_oz

    result = parmesan_reduction_oz
    return result

print(solution())