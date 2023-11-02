def solution():
    # Define the amount of flour each person brought in pounds
    katy_flour = 3 * 5
    wendi_flour = 2 * katy_flour
    carrie_flour = wendi_flour - 5

    # Convert the flour amounts from pounds to ounces
    katy_flour_oz = katy_flour * 16
    carrie_flour_oz = carrie_flour * 16

    # Calculate how much more flour Carrie brought than Katy in ounces
    diff_flour = carrie_flour_oz - katy_flour_oz
    result = diff_flour
    return result

print(solution())