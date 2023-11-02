def solution():
    # Calculate the total number of blueberries and muffins made
    total_blueberries = 3 * 200  # each carton has 200 blueberries
    blueberry_muffins = total_blueberries // 10
    total_muffins = blueberry_muffins + 60

    # Calculate the percentage of muffins that have blueberries
    blueberry_percentage = (blueberry_muffins / total_muffins) * 100
    result = blueberry_percentage
    return result

print(solution())