def solution():
    total_oranges = 55  # Salaria gets 55 good oranges per month
    good_oranges_from_tree_a = 10 * 0.6  # Tree A gives 10 oranges per month and 60% are good
    good_oranges_from_tree_b = 15 * (1/3)  # Tree B gives 15 oranges per month and 1/3 are good
    total_good_oranges = good_oranges_from_tree_a + good_oranges_from_tree_b  # Salaria gets a total of good oranges from both trees
    total_trees = (total_oranges / total_good_oranges) * 2  # Salaria has 50% of tree A and 50% of tree B, so she has 2 trees in total
    result = total_trees
    return result

print(solution())