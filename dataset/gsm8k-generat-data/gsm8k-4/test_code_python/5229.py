def solution():
    """Mikey likes his honey cluster of oats cereal. In each spoonful, there are 4 clusters of oats. In each bowl of cereal, he gets 25 spoonfuls of cereal. If each box of cereal contains 500 clusters of oats, how many bowlfuls of cereal are in each box?"""
    # Define the number of clusters in each bowl of cereal
    clusters_per_bowl = 4 * 25

    # Calculate the number of bowlfuls in each box
    bowlfuls_per_box = 500 / clusters_per_bowl

    result = bowlfuls_per_box
    return result

print(solution())