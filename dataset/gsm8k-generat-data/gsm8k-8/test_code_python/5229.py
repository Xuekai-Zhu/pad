def solution():
    # Calculate the total number of clusters in each box of cereal
    clusters_per_box = 500

    # Calculate the total number of clusters in each bowl of cereal
    clusters_per_bowl = 4 * 25

    # Calculate the number of bowlfuls of cereal in each box
    bowlfuls_per_box = clusters_per_box / clusters_per_bowl
    result = bowlfuls_per_box
    return result

print(solution())