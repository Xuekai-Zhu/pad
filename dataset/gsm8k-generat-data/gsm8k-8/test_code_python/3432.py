def solution():
    # Define the number of packs used
    own_packs = 3
    neighbor_packs = 2

    # Calculate the total number of balloons used
    total_balloons = (own_packs + neighbor_packs) * 6

    # Split the balloons evenly
    split_balloons = total_balloons / 2

    # Subtract Milly's extra balloons
    floretta_balloons = split_balloons - 7
    result = floretta_balloons
    return result

print(solution())