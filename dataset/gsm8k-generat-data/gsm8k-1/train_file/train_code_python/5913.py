def solution():
    """Salaria is growing oranges this summer. She bought two types of trees. She has 50% of tree A and 50% of tree B. Tree A gives her 10 oranges a month and 60% are good. Tree B gives her 15 oranges and 1/3 are good. If she gets 55 good oranges per month, how many total trees does she have?"""
    total_oranges = 55
    oranges_from_tree_a = 10
    good_oranges_percent_a = 60
    oranges_from_tree_b = 15
    good_oranges_percent_b = 33.33
    total_trees = (total_oranges / ((oranges_from_tree_a * (good_oranges_percent_a / 100)) + (oranges_from_tree_b * (good_oranges_percent_b / 100)))) * 2
    result = total_trees
    return result

print(solution())