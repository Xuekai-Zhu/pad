def solution():
    # Calculate the total number of blueberries
    total_blueberries = 3 * 200

    # Calculate the number of blueberry muffins that can be made
    blueberry_muffins = total_blueberries // 10

    # Calculate the total number of muffins
    total_muffins = blueberry_muffins + 60

    # Calculate the percentage of muffins with blueberries
    percent_blueberry_muffins = (blueberry_muffins / total_muffins) * 100
    result = percent_blueberry_muffins
    return result

print(solution())