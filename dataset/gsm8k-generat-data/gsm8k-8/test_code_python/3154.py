def solution():
    # Calculate the total number of pies
    total_pies = 3 * 11

    # Calculate the number of pies remaining after Tiffany eats 4
    remaining_pies = total_pies - 4

    # Calculate the number of cans of whipped cream needed to cover the remaining pies
    cans_of_whipped_cream = 2 * remaining_pies
    
    result = cans_of_whipped_cream
    return result

print(solution())