def solution():
    """Milly and Floretta are having a water balloon fight in their garden. They use 3 packs of their own water balloons and also use 2 packs of a neighbor’s water balloons. Each pack of water balloons contains 6 balloons. Milly and Floretta fill all of the balloons then split them evenly, but Milly takes an extra 7 balloons when Floretta isn't looking. How many water balloons is Floretta left with?"""
    # Define the number of packs of water balloons used
    own_packs = 3
    neighbor_packs = 2

    # Define the number of balloons per pack
    balloons_per_pack = 6

    # Calculate the total number of balloons
    total_balloons = (own_packs + neighbor_packs) * balloons_per_pack

    # Split the balloons evenly between Milly and Floretta
    floretta_balloons = total_balloons / 2

    # Subtract the extra balloons that Milly took
    floretta_balloons -= 7

    # Display the number of balloons Floretta has left
    result = floretta_balloons
    return result

print(solution())