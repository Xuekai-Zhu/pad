def solution():
    bill_width = 48
    bill_height = 100
    bob_width = 70
    bob_height = 60
    weight_per_sq_inch = 4 # oz
    oz_per_lb = 16 # 16 ounces per pound

    # Calculate the area of each TV screen
    bill_area = bill_width * bill_height
    bob_area = bob_width * bob_height

    # Calculate the weight of each TV
    bill_weight = bill_area * weight_per_sq_inch
    bob_weight = bob_area * weight_per_sq_inch

    # Calculate the weight difference in pounds
    weight_diff = (bob_weight - bill_weight) / oz_per_lb
    result = weight_diff
    return result

print(solution())