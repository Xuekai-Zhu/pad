def solution():
    num_apples = 10000
    apples_per_box = 50
    box_price = 35

    # Calculate the total number of boxes of apples Travis can sell
    total_boxes = num_apples / apples_per_box

    # Calculate the total amount of money Travis can earn from selling the boxes of apples
    total_earnings = total_boxes * box_price
    result = total_earnings
    return result

print(solution())