def solution():
    normal_tree_production = 60  # lemons per year for a normal lemon tree
    engineered_tree_production = normal_tree_production * 1.5  # lemons per year for an engineered lemon tree
    num_trees = 50 * 30  # total number of trees in the grove
    total_production = num_trees * engineered_tree_production  # total lemon production per year from all trees
    lemon_production_5_years = total_production * 5  # lemon production in 5 years
    result = lemon_production_5_years
    return result

print(solution())