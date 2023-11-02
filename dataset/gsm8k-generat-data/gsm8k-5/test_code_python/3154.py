def solution():
    pies_baked = 3 * 11  # Billie bakes 3 pies per day for 11 days, a total of 33 pies
    pies_remaining = pies_baked - 4  # Tiffany eats 4 pies, so there are 29 pies remaining
    whipped_cream_per_pie = 2  # It takes 2 cans of whipped cream to cover 1 pie

    # Calculate the total cans of whipped cream needed to cover the remaining pies
    total_whipped_cream_needed = pies_remaining * whipped_cream_per_pie
    result = total_whipped_cream_needed
    return result

print(solution())