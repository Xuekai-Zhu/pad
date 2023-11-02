def solution():
    num_nickels = 5
    num_nickels_taken = 2
    gum_per_nickel = 2

    # Calculate the total number of nickels used for gum
    total_nickels_for_gum = num_nickels - num_nickels_taken

    # Calculate the total number of pieces of gum received
    total_gum_pieces = total_nickels_for_gum * gum_per_nickel
    result = total_gum_pieces
    return result

print(solution())