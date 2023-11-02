def solution():
    num_cartons = 3
    blueberries_per_carton = 200
    blueberries_per_muffin = 10
    cinnamon_muffins = 60

    # Calculate the total number of blueberries Mason has
    total_blueberries = num_cartons * blueberries_per_carton

    # Calculate the number of blueberry muffins he can make
    blueberry_muffins = total_blueberries // blueberries_per_muffin

    # Calculate the total number of muffins he made
    total_muffins = blueberry_muffins + cinnamon_muffins

    # Calculate the percentage of muffins that have blueberries
    percent_blueberry_muffins = (blueberry_muffins / total_muffins) * 100
    result = percent_blueberry_muffins
    return result

print(solution())