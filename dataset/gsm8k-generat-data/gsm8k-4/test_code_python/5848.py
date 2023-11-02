def solution():
    """Two boxes for carrying oranges with a capacity of 80 and 50 were filled with 3/4 and 3/5 of the way full with oranges, respectively. Calculate the total number of oranges the boxes have together."""
    # Calculate the number of oranges in the first box
    box1_oranges = 80 * (3/4)

    # Calculate the number of oranges in the second box
    box2_oranges = 50 * (3/5)

    # Calculate the total number of oranges
    total_oranges = box1_oranges + box2_oranges

    result = total_oranges
    return result

print(solution())