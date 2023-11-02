def solution():
    apples_bought = 6  # Mary bought 6 apples
    trees_planted = 2  # For every apple Mary eats, she plants 2 trees
    total_trees_planted = apples_bought * trees_planted  # Calculate the total number of trees Mary planted
    remaining_apples = total_trees_planted + apples_bought  # Calculate how many apples Mary had left after planting the trees

    # Calculate how many apples Mary ate
    apples_ate = apples_bought - remaining_apples
    result = apples_ate
    return result

print(solution())