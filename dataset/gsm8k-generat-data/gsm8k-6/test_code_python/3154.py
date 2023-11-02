def solution():
    # Calculate the number of pies baked by Billie
    num_pies = 3 * 11  # baked 3 pumpkin pies for 11 days

    # Calculate the number of pies left after Tiffany eats 4
    pies_left = num_pies - 4

    # Calculate the number of cans of whipped cream needed to cover the remaining pies
    cans_whipped_cream = 2 * pies_left  # takes 2 cans of whipped cream to cover 1 pie
    result = cans_whipped_cream
    return result

print(solution())