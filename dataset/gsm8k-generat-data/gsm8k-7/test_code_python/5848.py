def solution():
    box1_capacity = 80
    box1_fill_percent = 0.75  # 3/4 full

    box2_capacity = 50
    box2_fill_percent = 0.6  # 3/5 full

    # Calculate the total number of oranges in box 1
    box1_num_oranges = box1_capacity * box1_fill_percent

    # Calculate the total number of oranges in box 2
    box2_num_oranges = box2_capacity * box2_fill_percent

    # Calculate the total number of oranges in both boxes together
    total_num_oranges = box1_num_oranges + box2_num_oranges
    result = total_num_oranges
    return result

print(solution())