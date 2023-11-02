def solution():
    roses_per_table_decoration = 12  # Mrs. Dunbar uses 12 white roses per table decoration
    roses_per_bouquet = 5  # Mrs. Dunbar uses 5 white roses per bouquet
    num_table_decorations = 7  # Mrs. Dunbar needs to make 7 table decorations
    num_bouquets = 5  # Mrs. Dunbar needs to make 5 bouquets

    # Calculate the total number of white roses needed for table decorations
    total_roses_for_table_decorations = roses_per_table_decoration * num_table_decorations

    # Calculate the total number of white roses needed for bouquets
    total_roses_for_bouquets = roses_per_bouquet * num_bouquets

    # Calculate the total number of white roses needed for all floral arrangements
    total_roses = total_roses_for_table_decorations + total_roses_for_bouquets
    result = total_roses
    return result

print(solution())