def solution():
     type_a_trees = 0.5
     type_b_trees = 0.5
     oranges_from_a = 10
     oranges_from_b = 15
     good_from_a = 0.6
     good_from_b = 1/3
     total_good_oranges = 55
     
     total_oranges_from_a = type_a_trees * oranges_from_a
     total_oranges_from_b = type_b_trees * oranges_from_b
     total_oranges = total_oranges_from_a + total_oranges_from_b
     
     good_oranges_from_a = total_oranges_from_a * good_from_a
     good_oranges_from_b = total_oranges_from_b * good_from_b
     
     total_trees = total_good_oranges / (good_oranges_from_a + good_oranges_from_b)
     result = total_trees
     return result

print(solution())