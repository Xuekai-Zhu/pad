def solution():
    """Every day, Billie bakes 3 pumpkin pies for 11 days and puts them in the refrigerator.  It takes 2 cans of whipped cream to cover 1 pie.  If Tiffany comes over and eats 4 pies, how many cans of whipped cream does Billie need to buy to cover the remaining pies?"""
    # Define the number of pumpkin pies baked by Billie each day
    pies_per_day = 3

    # Define the number of days Billie bakes the pumpkin pies
    days_baked = 11

    # Calculate the total number of pumpkin pies baked by Billie
    total_pies = pies_per_day * days_baked

    # Calculate the number of pumpkin pies remaining after Tiffany eats 4
    remaining_pies = total_pies - 4

    # Calculate the number of cans of whipped cream needed to cover the remaining pies
    cans_needed = remaining_pies * 2

    # Display the number of cans of whipped cream needed
    result = cans_needed
    return result

print(solution())