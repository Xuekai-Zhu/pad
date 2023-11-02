def solution():
    """There are 10 bags with 30 oranges each on a truck. A total of 50 pieces of oranges are rotten. Thirty pieces of oranges will be kept for making orange juice and the rest will be sold. How many pieces of oranges will be sold?"""
    bags = 10
    oranges_per_bag = 30
    total_oranges = bags * oranges_per_bag
    rotten_oranges = 50
    good_oranges = total_oranges - rotten_oranges
    oranges_for_juice = 30
    oranges_to_sell = good_oranges - oranges_for_juice
    result = oranges_to_sell
    return result

print(solution())