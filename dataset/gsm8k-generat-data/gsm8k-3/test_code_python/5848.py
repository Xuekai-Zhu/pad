def solution():
    """Two boxes for carrying oranges with a capacity of 80 and 50 were filled with 3/4 and 3/5 of the way full with oranges, respectively. Calculate the total number of oranges the boxes have together."""
    # Calculate the number of oranges in the first box
    box1_capacity = 80
    box1_fill = 3/4
    box1_oranges = box1_capacity * box1_fill

    # Calculate the number of oranges in the second box
    box2_capacity = 50
    box2_fill = 3/5
    box2_oranges = box2_capacity * box2_fill

    # Calculate the total number of oranges
    total_oranges = box1_oranges + box2_oranges

    # Display the total number of oranges
    result = total_oranges
    return result

print(solution())