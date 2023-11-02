def solution():
    num_boxes = 48
    erasers_per_box = 24
    price_per_eraser = 0.75

    # Calculate the total number of erasers
    total_erasers = num_boxes * erasers_per_box

    # Calculate the total amount of money made
    total_money = total_erasers * price_per_eraser
    result = total_money
    return result

print(solution())