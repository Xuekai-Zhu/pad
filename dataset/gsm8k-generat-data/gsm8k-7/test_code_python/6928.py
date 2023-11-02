def solution():
    boxes_per_week = 10
    apples_per_box = 300
    sell_percentage = 0.75  # 3/4 of the stock sold
    total_apples = boxes_per_week * apples_per_box

    # Calculate the number of apples sold in a week
    num_sold = total_apples * sell_percentage

    # Calculate the number of apples remaining
    num_remaining = total_apples - num_sold
    result = num_remaining
    return result

print(solution())