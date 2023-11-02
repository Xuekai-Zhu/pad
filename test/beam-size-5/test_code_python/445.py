def solution():
    
    # Define the number of packets and the number of pieces of colors per packet
    packets = 10
    pieces_per_packet = 8

    # Calculate the total number of pieces of colors
    total_colors = (packets * pieces_per_packet) + (packets * pieces_per_packet)

    # return the result
    result = total_colors
    return result

print(solution())