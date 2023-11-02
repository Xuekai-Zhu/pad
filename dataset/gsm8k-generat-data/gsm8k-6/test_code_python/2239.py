def solution():
    # Calculate the total number of oranges picked by Frank, Betty and Bill
    total_oranges_picked = 15 + 12 + (3 * (15 + 12))  # Frank picked three times the number Betty and Bill picked combined

    # Calculate the total number of trees that Frank planted
    total_trees_planted = 2 * total_oranges_picked

    # Calculate the total number of oranges available for Philip to pick
    total_oranges_for_Philip = total_trees_planted * 5  # each tree contains 5 oranges

    result = total_oranges_for_Philip
    return result

print(solution())