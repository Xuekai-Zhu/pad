def solution():
    """Mason has 3 cartons of 200 blueberries. He makes as many muffins as he can with 10 blueberries per muffin. Then he makes 60 cinnamon muffins. What percentage of all the muffins he made have blueberries?"""
    blueberry_cartons = 3
    blueberries_per_carton = 200
    total_blueberries = blueberry_cartons * blueberries_per_carton
    muffins_from_blueberries = total_blueberries // 10
    total_muffins = muffins_from_blueberries + 60
    percentage_blueberry_muffins = (muffins_from_blueberries / total_muffins) * 100
    result = percentage_blueberry_muffins
    return result

print(solution())