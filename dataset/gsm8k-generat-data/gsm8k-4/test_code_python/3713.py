def solution():
    """Lovely cuts her birthday cake into 12 equal pieces. Only one-fourth of the cake was eaten by her visitors and the rest were kept. How many slices of cake were kept?"""
    # Define the number of cake slices
    cake_slices = 12

    # Calculate the number of slices eaten by visitors
    eaten_slices = cake_slices * 0.25

    # Calculate the number of slices kept
    kept_slices = cake_slices - eaten_slices

    # Return the result
    result = kept_slices
    return result

print(solution())