def solution():
    
    mahogany_trees = 50
    narra_trees = 30
    total_fallen_trees = 5
    narra_fallen = (total_fallen_trees - 1) // 2 
    mahogany_fallen = total_fallen_trees - narra_fallen
    narra_planted = 2 * narra_fallen
    mahogany_planted = 3 * mahogany_fallen
    total_narra = narra_trees - narra_fallen + narra_planted
    total_mahogany = mahogany_trees - mahogany_fallen + mahogany_planted
    total_trees = total_narra + total_mahogany
    result = total_trees
    return result

print(solution())