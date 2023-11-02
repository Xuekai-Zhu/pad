def solution():
    """Frank and his friends Betty and Bill went to their farm and picked oranges to eat. Betty picked 15 oranges and Bill picked 12 oranges. Frank picked three times the number that Betty and Bill picked combined. Frank then planted 2 seeds from each of his oranges into the ground and waited 20 years for each seed to turn into a beautiful orange tree. If each orange tree contains 5 oranges for Frank's son Philip to pick, how many oranges are there for Philip to pick in total?"""
    # Calculate the total number of oranges picked by Betty and Bill
    betty_oranges = 15
    bill_oranges = 12
    total_oranges = betty_oranges + bill_oranges

    # Calculate the number of oranges picked by Frank
    frank_oranges = 3 * total_oranges

    # Calculate the number of orange trees Frank planted
    orange_trees = frank_oranges * 2

    # Calculate the total number of oranges on all the orange trees
    total_oranges_trees = orange_trees * 5

    result = total_oranges_trees
    return result

print(solution())