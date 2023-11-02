def solution():
    num_packets = 8
    pieces_per_packet = 7
    pieces_left = 2

    # Calculate the total number of pieces of gum Mitchell has
    total_pieces = num_packets * pieces_per_packet

    # Subtract the number of pieces left from the total
    pieces_chewed = total_pieces - pieces_left
    result = pieces_chewed
    return result

print(solution())