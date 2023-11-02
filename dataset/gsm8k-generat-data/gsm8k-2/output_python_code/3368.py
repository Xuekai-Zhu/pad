def solution():
    """Iris has a berry farm. Her brother and sister help her to pick up the berries and sell them to the market. Iris picked 30 blueberries, her sister picked 20 cranberries, and her brother was able to pick 10 raspberries. If 1/3 of the total berries they were able to pick are rotten and the remaining 1/2 of the fresh berries need to be kept, how many berries will they be able to sell?"""
    total_beries = 30 + 20 + 10
    rotten_beries = total_beries / 3
    fresh_beries = total_beries - rotten_beries
    sellable_beries = fresh_beries / 2
    result = sellable_beries
    return result

print(solution())