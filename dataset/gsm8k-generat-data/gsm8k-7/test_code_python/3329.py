def solution():
    num_amber_pieces = 20
    num_green_pieces = 35
    green_percentage = 0.25  # 25% of total glass

    # Calculate the total number of glass pieces Jerry swept up
    total_pieces = (num_amber_pieces + num_green_pieces) / green_percentage

    # Calculate the number of clear pieces
    clear_pieces = total_pieces - num_amber_pieces - num_green_pieces
    result = clear_pieces
    return result

print(solution())