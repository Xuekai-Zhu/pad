def solution():
    mason_bees_solitary = True
    mason_bees_efficient_pollinators = True
    apple_trees_grown_in_orchards = True
    if mason_bees_solitary and mason_bees_efficient_pollinators and apple_trees_grown_in_orchards:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())