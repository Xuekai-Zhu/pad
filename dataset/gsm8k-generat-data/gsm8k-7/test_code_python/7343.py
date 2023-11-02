def solution():
    total_earnings = 32
    num_pans = 2
    num_pieces_per_pan = 8

    # Calculate the total number of pieces of brownies
    total_pieces = num_pans * num_pieces_per_pan

    # Calculate the cost per piece of brownie
    cost_per_brownie = total_earnings / total_pieces
    result = cost_per_brownie
    return result

print(solution())