def solution():
    # Calculate the number of oranges in the first box
    box1_capacity = 80
    box1_fill_ratio = 3/4
    box1_oranges = box1_capacity * box1_fill_ratio

    # Calculate the number of oranges in the second box
    box2_capacity = 50
    box2_fill_ratio = 3/5
    box2_oranges = box2_capacity * box2_fill_ratio

    # Calculate the total number of oranges in both boxes
    total_oranges = box1_oranges + box2_oranges
    result = total_oranges
    return result

print(solution())