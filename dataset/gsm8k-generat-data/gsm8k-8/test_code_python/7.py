def solution():
    initial_weight = 0 # weight of the box before adding anything
    jellybeans_weight = 2 # weight of the first addition
    brownies_weight = jellybeans_weight * 3 # weight after adding brownies
    jellybeans_weight2 = 2 # weight of the second addition
    gummyworms_weight = brownies_weight * 2 # weight after adding gummy worms

    final_weight = initial_weight + jellybeans_weight + brownies_weight + jellybeans_weight2 + gummyworms_weight
    result = final_weight
    return result

print(solution())