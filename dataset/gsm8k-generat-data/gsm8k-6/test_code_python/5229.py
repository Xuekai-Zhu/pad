def solution():
    # Calculate the number of clusters of oats in each box of cereal
    clusters_per_box = 500

    # Calculate the number of spoonfuls of cereal in each box
    spoonfuls_per_box = clusters_per_box / 4  # 4 clusters in each spoonful
    # Calculate the number of bowlfuls of cereal in each box
    bowls_per_box = spoonfuls_per_box / 25  # 25 spoonfuls in each bowl
    result = bowls_per_box
    return result

print(solution())