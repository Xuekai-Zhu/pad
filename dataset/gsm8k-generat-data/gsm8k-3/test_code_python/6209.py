def solution():
    """Gilbert grows herbs in his yard to use in his cooking. At the beginning of the spring, he planted three basil bushes, a parsley plant, and two kinds of mint. Halfway through spring, one of the basil plants dropped seeds from a flower and made an extra basil plant grow. However, a rabbit came by the garden near the end of spring and ate all the mint. How many herb plants did Gilbert have when spring ended?"""
    # Define the starting number of each type of herb
    basil_bushes = 3
    parsley = 1
    mint = 2

    # Add the extra basil plant that grew from seeds
    basil_bushes += 1

    # Subtract the mint plants that were eaten by the rabbit
    mint -= 2

    # Calculate the total number of herb plants
    total_plants = basil_bushes + parsley + mint

    # Display the total number of herb plants
    result = total_plants
    return result

print(solution())