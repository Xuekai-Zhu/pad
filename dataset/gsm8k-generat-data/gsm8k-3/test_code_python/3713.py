def solution():
    """Lovely cuts her birthday cake into 12 equal pieces. Only one-fourth of the cake was eaten by her visitors and the rest were kept. How many slices of cake were kept?"""
    # Define the total number of pieces of cake
    total_pieces = 12

    # Calculate the number of pieces eaten by visitors
    eaten_pieces = total_pieces // 4

    # Calculate the number of pieces kept
    kept_pieces = total_pieces - eaten_pieces

    # Display the number of pieces kept
    result = kept_pieces
    return result

print(solution())