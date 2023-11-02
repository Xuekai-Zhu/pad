def solution():
    olga_stripes_per_shoe = 3
    rick_stripes_per_shoe = olga_stripes_per_shoe - 1
    hortense_stripes_per_shoe = olga_stripes_per_shoe * 2

    num_pairs_of_shoes = 6 # Assuming each person has one pair of shoes
    
    # Calculate the total number of stripes on Olga's shoes
    olga_total_stripes = olga_stripes_per_shoe * num_pairs_of_shoes

    # Calculate the total number of stripes on Rick's shoes
    rick_total_stripes = rick_stripes_per_shoe * num_pairs_of_shoes

    # Calculate the total number of stripes on Hortense's shoes
    hortense_total_stripes = hortense_stripes_per_shoe * num_pairs_of_shoes

    # Calculate the combined number of stripes on all pairs of shoes
    total_stripes = olga_total_stripes + rick_total_stripes + hortense_total_stripes
    
    result = total_stripes
    return result

print(solution())