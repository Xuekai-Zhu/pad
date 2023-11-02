def solution():
    # Calculate the total number of oranges picked by Dulce
    oranges_picked = (2/5) * 200  # Dulce picked 2/5 of the oranges from each tree and each tree has 200 fruits
    total_oranges_picked = oranges_picked * 8  # there are 8 orange trees on the farm
    # Calculate the total number of oranges remaining
    total_oranges_left = 200 * 8 - total_oranges_picked
    result = total_oranges_left
    return result

print(solution())