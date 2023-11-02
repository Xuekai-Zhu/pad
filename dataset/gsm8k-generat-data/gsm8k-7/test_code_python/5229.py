def solution():
    clusters_per_spoonful = 4
    spoonfuls_per_bowl = 25
    clusters_per_box = 500

    # Calculate the total number of clusters in each bowl of cereal
    clusters_per_bowl = clusters_per_spoonful * spoonfuls_per_bowl

    # Calculate the total number of bowlfuls in each box of cereal
    bowlfuls_per_box = clusters_per_box // clusters_per_bowl
    result = bowlfuls_per_box
    return result

print(solution())