def solution():
    """Beatrice bought ten packets of crayons for her Art class. Six of the packets had eight pieces of colors each, and the other four packets had sixteen pieces of colors each. How many colors of crayons did Beatrice buy in all?"""
    packets_1 = 6
    packets_2 = 4
    pieces_per_packet_1 = 8
    pieces_per_packet_2 = 16
    total_pieces = (packets_1 * pieces_per_packet_1) + (packets_2 * pieces_per_packet_2)
    result = total_pieces
    return result

print(solution())