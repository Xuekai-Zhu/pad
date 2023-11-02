def solution():
    
    blueberries_per_carton = 200
    total_blueberries = blueberries_per_carton * 3
    blueberries_per_muffin = 10
    blueberry_muffins = total_blueberries // blueberries_per_muffin
    total_muffins = blueberry_muffins + 60
    blueberry_percentage = (blueberry_muffins / total_muffins) * 100
    result = blueberry_percentage
    return result

print(solution())