def solution():
    num_bouquets = 5
    num_table_decorations = 7
    roses_per_table_decoration = 12
    roses_per_bouquet = 5

    # Calculate the total number of white roses needed for all table decorations
    total_roses_for_table_decorations = num_table_decorations * roses_per_table_decoration

    # Calculate the total number of white roses needed for all bouquets
    total_roses_for_bouquets = num_bouquets * roses_per_bouquet

    # Calculate the total number of white roses needed for all floral arrangements
    total_roses_needed = total_roses_for_table_decorations + total_roses_for_bouquets
    result = total_roses_needed
    return result

print(solution())