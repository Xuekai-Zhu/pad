def solution():
     pine_trees = 8
     pine_cones_dropped = pine_trees * 200
     pine_cones_on_roof = pine_cones_dropped * 0.3
     ounces_per_cone = 4
     total_ounces = pine_cones_on_roof * ounces_per_cone
     
     return total_ounces

print(solution())