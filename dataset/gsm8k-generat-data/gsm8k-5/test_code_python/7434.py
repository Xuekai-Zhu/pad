def solution():
    total_apples = 10000  # Travis has 10000 apples
    apples_per_box = 50  # Fifty apples can fit in each box
    boxes = total_apples / apples_per_box  # Calculate the total number of boxes
    box_price = 35  # Each box of apples sells for $35

    # Calculate the total amount Travis will be able to take home
    total_sales = boxes * box_price
    result = total_sales
    return result

print(solution())