def solution():
    box1_capacity = 80  # Box 1 has a capacity of 80 oranges
    box2_capacity = 50  # Box 2 has a capacity of 50 oranges
    box1_filled_fraction = 3/4  # Box 1 is filled 3/4 of the way full
    box2_filled_fraction = 3/5  # Box 2 is filled 3/5 of the way full

    # Calculate the number of oranges in each box
    box1_oranges = box1_capacity * box1_filled_fraction
    box2_oranges = box2_capacity * box2_filled_fraction

    # Calculate the total number of oranges in both boxes
    total_oranges = box1_oranges + box2_oranges
    result = total_oranges
    return result

print(solution())