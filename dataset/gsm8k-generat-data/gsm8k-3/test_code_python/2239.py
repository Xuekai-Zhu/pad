def solution():
    """Frank and his friends Betty and Bill went to their farm and picked oranges to eat. Betty picked 15 oranges and Bill picked 12 oranges. Frank picked three times the number that Betty and Bill picked combined. Frank then planted 2 seeds from each of his oranges into the ground and waited 20 years for each seed to turn into a beautiful orange tree. If each orange tree contains 5 oranges for Frank's son Philip to pick, how many oranges are there for Philip to pick in total?"""
    # Calculate the total number of oranges picked by Frank, Betty, and Bill
    total_oranges_picked = 15 + 12 + (3 * (15 + 12))

    # Calculate the total number of seeds planted by Frank
    total_seeds_planted = 2 * total_oranges_picked

    # Calculate the total number of trees grown
    total_trees_grown = total_seeds_planted * 20

    # Calculate the total number of oranges Philip can pick
    total_oranges_philip_can_pick = total_trees_grown * 5

    # Display the total number of oranges Philip can pick
    result = total_oranges_philip_can_pick
    return result

print(solution())