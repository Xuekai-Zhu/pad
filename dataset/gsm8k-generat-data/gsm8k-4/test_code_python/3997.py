def solution():
    """Mitchell is trying to chew as many pieces of gum at once as he can. He has 8 packets of gum, There are 7 pieces in each. If he chews all the gum except for 2 pieces, how many pieces does he chew at once?"""
    # Define the number of packets of gum and the number of pieces per packet
    num_packets = 8
    pieces_per_packet = 7

    # Calculate the total number of pieces of gum
    total_pieces = num_packets * pieces_per_packet

    # Calculate the number of pieces Mitchell chews at once
    pieces_chewed = total_pieces - 2

    # Return the result
    result = pieces_chewed
    return result

print(solution())