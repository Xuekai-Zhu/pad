def solution():
    """Mason has 3 cartons of 200 blueberries. He makes as many muffins as he can with 10 blueberries per muffin. Then he makes 60 cinnamon muffins. What percentage of all the muffins he made have blueberries?"""
    blueberries_per_carton = 200
    total_blueberries = blueberries_per_carton * 3
    blueberries_per_muffin = 10
    blueberry_muffins = total_blueberries // blueberries_per_muffin
    total_muffins = blueberry_muffins + 60
    blueberry_percentage = (blueberry_muffins / total_muffins) * 100
    result = blueberry_percentage
    return result

print(solution())