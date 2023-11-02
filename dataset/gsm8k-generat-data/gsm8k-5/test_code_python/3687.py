def solution():
    total_blueberries = 3 * 200  # Mason has 3 cartons of 200 blueberries each
    blueberry_muffins = total_blueberries // 10  # Mason makes as many blueberry muffins as possible using 10 blueberries per muffin
    total_muffins = blueberry_muffins + 60  # Mason also makes 60 cinnamon muffins
    blueberry_percentage = (blueberry_muffins / total_muffins) * 100  # Calculate the percentage of muffins that have blueberries
    result = blueberry_percentage
    return result

print(solution())