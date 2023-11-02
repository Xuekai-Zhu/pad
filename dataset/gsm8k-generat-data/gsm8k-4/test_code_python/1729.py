def solution():
    """Calvin is a bug collector. In his collection, he has 12 giant roaches, 3 scorpions, half as many crickets as roaches, and twice as many caterpillars as scorpions. How many insects does Calvin have in his collection?"""
    # Define the number of giant roaches
    giant_roaches = 12

    # Define the number of scorpions
    scorpions = 3

    # Calculate the number of crickets
    crickets = giant_roaches / 2

    # Calculate the number of caterpillars
    caterpillars = scorpions * 2

    # Calculate the total number of insects
    total_insects = giant_roaches + scorpions + crickets + caterpillars

    # return the result
    result = total_insects
    return result

print(solution())