def solution():
    # Calculate the number of trees cut down by James in the first 2 days
    james_total_trees = 20 + 20
    # Calculate the number of trees cut down by James and his brothers in the next 3 days 
    james_tree_percentage = 0.20 # James' brothers cut 20% fewer trees per day
    james_trees_per_day = 20
    james_tree_cut = james_trees_per_day * james_tree_percentage
    james_bro_tree_cut = james_trees_per_day - james_tree_cut
    total_trees_james_bro = ((20 + 20) * james_bro_tree_cut) * 3
    # Calculate the total number of trees cut down
    total_trees = james_total_trees + total_trees_james_bro
    result = total_trees
    return result

print(solution())