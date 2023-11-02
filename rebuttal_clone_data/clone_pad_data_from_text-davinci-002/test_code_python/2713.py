def solution():
     width_apple_trees = 10
     distance_between_apple_trees = 12
     width_peach_trees = 12
     distance_between_peach_trees = 15
     total_apple_tree_space = (width_apple_trees * 2) + (distance_between_apple_trees * 2)
     total_peach_tree_space = (width_peach_trees * 2) + (distance_between_peach_trees * 2)
     total_space = total_apple_tree_space + total_peach_tree_space
     
     return total_space

print(solution())