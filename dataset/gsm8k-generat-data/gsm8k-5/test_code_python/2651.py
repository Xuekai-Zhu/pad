def solution():
    axe_sharpening_cost = 5  # It costs $5 to sharpen Felix's axe
    total_sharpening_cost = 35  # Felix spent $35 on axe sharpening
    sharpening_count = total_sharpening_cost // axe_sharpening_cost  # Calculate the number of times Felix sharpened his axe
    trees_per_sharpening = 13  # Felix chops down 13 trees before needing to sharpen his axe

    # Calculate the minimum number of trees Felix has chopped down
    min_trees_chopped = sharpening_count * trees_per_sharpening
    result = min_trees_chopped
    return result

print(solution())