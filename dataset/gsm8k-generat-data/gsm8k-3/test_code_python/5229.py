def solution():
    """Mikey likes his honey cluster of oats cereal.  In each spoonful, there are 4 clusters of oats.  In each bowl of cereal, he gets 25 spoonfuls of cereal.  If each box of cereal contains 500 clusters of oats, how many bowlfuls of cereal are in each box?"""
    # Define the number of clusters of oats in each spoonful
    CLUSTERS_PER_SPOONFUL = 4

    # Define the number of spoonfuls in each bowl
    SPOONFULS_PER_BOWL = 25

    # Define the number of clusters of oats in each box
    CLUSTERS_PER_BOX = 500

    # Calculate the number of clusters of oats in each bowl
    clusters_per_bowl = CLUSTERS_PER_SPOONFUL * SPOONFULS_PER_BOWL

    # Calculate the number of bowlfuls in each box
    bowlfuls_per_box = CLUSTERS_PER_BOX // clusters_per_bowl

    # Display the number of bowlfuls in each box
    result = bowlfuls_per_box
    return result

print(solution())