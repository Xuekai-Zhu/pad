def solution():
    # Define the number of cookies baked
    oatmeal_raisin = 3 * 12
    sugar = 2 * 12
    chocolate_chip = 4 * 12

    # Calculate the number of cookies given away
    oatmeal_raisin_given = 2 * 12
    sugar_given = 1.5 * 12
    chocolate_chip_given = 2.5 * 12

    # Calculate the total number of cookies kept
    total_kept = oatmeal_raisin + sugar + chocolate_chip - oatmeal_raisin_given - sugar_given - chocolate_chip_given
    result = total_kept
    return result

print(solution())