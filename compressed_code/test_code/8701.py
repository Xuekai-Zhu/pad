def solution():
    
    blueberry_cartons = 3
    blueberries_per_carton = 200
    total_blueberries = blueberry_cartons * blueberries_per_carton
    muffins_from_blueberries = total_blueberries // 10
    total_muffins = muffins_from_blueberries + 60
    percentage_blueberry_muffins = (muffins_from_blueberries / total_muffins) * 100
    result = percentage_blueberry_muffins
    return result

print(solution())