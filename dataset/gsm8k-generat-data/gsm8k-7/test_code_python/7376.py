def solution():
    num_days = 5
    num_pieces = 40

    # Calculate the total number of servings of jerky that Janette will eat
    total_servings = num_days * 4

    # Calculate the number of pieces of jerky that Janette will have left after the trip
    remaining_pieces = num_pieces - total_servings

    # Calculate the number of pieces of jerky that Janette will give to her brother
    given_pieces = remaining_pieces / 2

    # Calculate the final number of pieces of jerky that Janette will have left
    final_num_pieces = remaining_pieces - given_pieces
    result = final_num_pieces
    return result

print(solution())