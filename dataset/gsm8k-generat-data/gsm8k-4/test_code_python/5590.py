def solution():
    """A desert has 3/5 fewer palm trees than a nearby forest, which has 5000 palm trees. How many palm trees are there in both the desert and the forest combined?"""
    # Define the number of palm trees in the forest
    forest_palms = 5000

    # Calculate the number of palm trees in the desert
    desert_palms = forest_palms * (2/5)

    # Calculate the total number of palm trees
    total_palms = forest_palms + desert_palms

    # return the result
    result = total_palms
    return result

print(solution())