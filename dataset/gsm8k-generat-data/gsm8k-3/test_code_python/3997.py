def solution():
    """Mitchell is trying to chew as many pieces of gum at once as he can. He has 8 packets of gum, There are 7 pieces in each. If he chews all the gum except for 2 pieces, how many pieces does he chew at once?"""
    # Define the number of packets and pieces of gum
    packets = 8
    pieces_per_packet = 7

    # Calculate the total number of pieces of gum
    total_pieces = packets * pieces_per_packet

    # Subtract 2 from the total pieces to find how many pieces Mitchell chews at once
    pieces_chewed = total_pieces - 2

    # Display the number of pieces Mitchell chews at once
    result = pieces_chewed
    return result

print(solution())