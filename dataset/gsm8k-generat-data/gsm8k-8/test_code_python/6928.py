def solution():
    # Define the number of boxes and apples in each box
    boxes = 10
    apples_per_box = 300

    # Calculate the total number of apples in the order
    total_apples = boxes * apples_per_box

    # Calculate the number of apples sold in the week
    sold_apples = 0.75 * total_apples

    # Calculate the number of apples not sold
    not_sold_apples = total_apples - sold_apples
    result = not_sold_apples
    return result

print(solution())