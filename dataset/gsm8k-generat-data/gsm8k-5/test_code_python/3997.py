def solution():
    packets_of_gum = 8  # Mitchell has 8 packets of gum
    pieces_in_packet = 7  # Each packet has 7 pieces of gum
    total_pieces = packets_of_gum * pieces_in_packet  # Calculate the total number of gum pieces

    # Subtract 2 pieces that he didn't chew
    pieces_chewed = total_pieces - 2
    result = pieces_chewed
    return result

print(solution())