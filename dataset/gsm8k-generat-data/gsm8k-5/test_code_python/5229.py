def solution():
    clusters_per_spoonful = 4  # Each spoonful of cereal contains 4 clusters of oats
    spoonfuls_per_bowl = 25  # Each bowl of cereal has 25 spoonfuls
    clusters_per_box = 500  # Each box of cereal contains 500 clusters of oats

    # Calculate the total number of spoonfuls in each box of cereal
    spoonfuls_per_box = clusters_per_box / clusters_per_spoonful / spoonfuls_per_bowl
    result = spoonfuls_per_box
    return result

print(solution())