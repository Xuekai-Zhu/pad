def solution():
    """Milly and Floretta are having a water balloon fight in their garden. They use 3 packs of their own water balloons and also use 2 packs of a neighbor’s water balloons. Each pack of water balloons contains 6 balloons. Milly and Floretta fill all of the balloons then split them evenly, but Milly takes an extra 7 balloons when Floretta isn't looking. How many water balloons is Floretta left with?"""
    # Define the number of packs of water balloons used
    own_packs = 3
    neighbor_packs = 2

    # Define the number of water balloons in each pack
    balloons_per_pack = 6

    # Calculate the total number of water balloons
    total_balloons = (own_packs + neighbor_packs) * balloons_per_pack

    # Calculate how many balloons each girl gets
    balloons_per_girl = total_balloons // 2

    # Subtract the 7 extra balloons Milly takes from Floretta
    floretta_balloons = balloons_per_girl - 7

    result = floretta_balloons
    return result

print(solution())