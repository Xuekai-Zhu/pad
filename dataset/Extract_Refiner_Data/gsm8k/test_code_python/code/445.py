def solution():
    
    # Define the number of packets and the number of pieces of colors per packet
    num_packets = 10
    pieces_per_packet_1 = 8
    pieces_per_packet_2 = 16

    # Calculate the total number of pieces of colors in the first six packets
    total_pieces_1 = pieces_per_packet_1 * 6

    # Calculate the total number of pieces of colors in the other four packets
    total_pieces_2 = pieces_per_packet_2 * 4

    # Calculate the total number of pieces of colors
    total_pieces = total_pieces_1 + total_pieces_2

    # return the result
    result = total_pieces
    return result

print(solution())