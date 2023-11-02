def solution():
    # Define the initial total number of gum pieces
    total_gum_pieces = 100

    # Calculate the number of pieces Elyse gave to Rick
    rick_gum_pieces = total_gum_pieces / 2

    # Calculate the number of pieces Shane received from Rick
    shane_gum_pieces = rick_gum_pieces / 2

    # Calculate the remaining number of gum pieces Shane has
    remaining_gum_pieces = shane_gum_pieces - 11
    result = remaining_gum_pieces
    return result

print(solution())