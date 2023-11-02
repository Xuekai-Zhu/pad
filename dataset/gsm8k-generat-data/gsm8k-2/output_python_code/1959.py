def solution():
    """There are 10 bags with 30 oranges each on a truck. A total of 50 pieces of oranges are rotten. Thirty pieces of oranges will be kept for making orange juice and the rest will be sold. How many pieces of oranges will be sold?"""
    total_oranges = 10 * 30
    rotten_oranges = 50
    good_oranges = total_oranges - rotten_oranges
    juice_oranges = 30
    sold_oranges = good_oranges - juice_oranges
    result = sold_oranges
    return result

print(solution())