def solution():
    """Mason has 3 cartons of 200 blueberries. He makes as many muffins as he can with 10 blueberries per muffin. Then he makes 60 cinnamon muffins. What percentage of all the muffins he made have blueberries?"""
    # Define the number of cartons and blueberries per carton
    cartons = 3
    blueberries_per_carton = 200

    # Calculate the total number of blueberries
    total_blueberries = cartons * blueberries_per_carton

    # Calculate the number of blueberry muffins that can be made
    blueberry_muffins = total_blueberries // 10

    # Calculate the total number of muffins
    total_muffins = blueberry_muffins + 60

    # Calculate the percentage of muffins that have blueberries
    percentage_blueberry_muffins = (blueberry_muffins / total_muffins) * 100

    # Return the result
    result = percentage_blueberry_muffins
    return result

print(solution())