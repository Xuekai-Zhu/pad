def solution():
    num_pies_baked_per_day = 3
    num_days = 11
    num_pies_eaten_by_tiffany = 4
    num_cans_of_whipped_cream_per_pie = 2

    # Calculate the total number of pies baked by Billie
    total_pies_baked = num_pies_baked_per_day * num_days

    # Calculate the total number of pies remaining after Tiffany eats some
    total_pies_remaining = total_pies_baked - num_pies_eaten_by_tiffany

    # Calculate the total number of cans of whipped cream needed to cover the remaining pies
    total_cans_of_whipped_cream = total_pies_remaining * num_cans_of_whipped_cream_per_pie
    result = total_cans_of_whipped_cream
    return result

print(solution())