def solution():
    """Mikey likes his honey cluster of oats cereal. In each spoonful, there are 4 clusters of oats. In each bowl of cereal, he gets 25 spoonfuls of cereal. If each box of cereal contains 500 clusters of oats, how many bowlfuls of cereal are in each box?"""
    clusters_per_spoonful = 4
    spoonfuls_per_bowl = 25
    clusters_per_bowl = clusters_per_spoonful * spoonfuls_per_bowl
    clusters_per_box = 500
    bowlfuls_per_box = clusters_per_box / clusters_per_bowl
    result = bowlfuls_per_box
    return result

print(solution())