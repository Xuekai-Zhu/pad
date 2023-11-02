def solution():
    """Mitchell is trying to chew as many pieces of gum at once as he can. He has 8 packets of gum, There are 7 pieces in each. If he chews all the gum except for 2 pieces, how many pieces does he chew at once?"""
    packets_of_gum = 8
    pieces_per_packet = 7
    total_pieces = packets_of_gum * pieces_per_packet
    pieces_chewed = total_pieces - 2
    result = pieces_chewed
    return result

print(solution())