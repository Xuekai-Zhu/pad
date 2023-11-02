def solution():
    # Calculate the total number of oranges on all trees
    total_oranges = 8 * 200

    # Calculate the number of oranges Dulce picks from each tree
    dulce_picks = 2/5

    # Calculate the total number of oranges Dulce picks
    dulce_total = total_oranges * dulce_picks

    # Calculate the total number of oranges remaining on the trees
    remaining_oranges = total_oranges - dulce_total
    result = remaining_oranges
    return result

print(solution())