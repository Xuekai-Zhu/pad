def solution():
    
    clusters_per_spoonful = 4
    spoonfuls_per_bowl = 25
    clusters_per_box = 500
    bowls_per_box = (clusters_per_box // clusters_per_spoonful) // spoonfuls_per_bowl
    result = bowls_per_box
    return result

print(solution())