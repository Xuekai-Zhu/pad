def solution():
    num_shepherds_pieces_per_pie = 4
    num_chicken_pieces_per_pie = 5
    num_shepherds_pieces_ordered = 52
    num_chicken_pieces_ordered = 80

    # Calculate the total number of shepherd's pies sold
    total_shepherds_pies = num_shepherds_pieces_ordered / num_shepherds_pieces_per_pie

    # Calculate the total number of chicken pot pies sold
    total_chicken_pies = num_chicken_pieces_ordered / num_chicken_pieces_per_pie

    # Calculate the total number of all pies sold
    total_pies_sold = total_shepherds_pies + total_chicken_pies
    result = total_pies_sold
    return result

print(solution())