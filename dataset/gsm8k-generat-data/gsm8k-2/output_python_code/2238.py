def solution():
    """Frank and his friends Betty and Bill went to their farm and picked oranges to eat. Betty picked 15 oranges and Bill picked 12 oranges. Frank picked three times the number that Betty and Bill picked combined. Frank then planted 2 seeds from each of his oranges into the ground and waited 20 years for each seed to turn into a beautiful orange tree. If each orange tree contains 5 oranges for Frank's son Philip to pick, how many oranges are there for Philip to pick in total?"""
    betty_oranges = 15
    bill_oranges = 12
    combined_oranges = betty_oranges + bill_oranges
    frank_oranges = 3 * combined_oranges
    total_seeds = frank_oranges * 2
    total_trees = total_seeds
    total_oranges = total_trees * 5
    result = total_oranges
    return result

print(solution())