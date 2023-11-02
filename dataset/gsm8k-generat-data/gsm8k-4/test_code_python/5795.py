def solution():
    """Ariana heard the news that a new grocery store had opened up in their town, so she decided to buy some flowers for her house. She bought a bunch of 40 flowers, 2/5 of which were roses, 10 were tulips, and the rest were carnations. How many carnations did she buy?"""
    # Define the total number of flowers in the bunch
    total_flowers = 40

    # Calculate the number of roses in the bunch
    roses = total_flowers * (2/5)

    # Calculate the number of tulips in the bunch
    tulips = 10

    # Calculate the number of carnations in the bunch
    carnations = total_flowers - roses - tulips

    # return the result
    result = carnations
    return result

print(solution())