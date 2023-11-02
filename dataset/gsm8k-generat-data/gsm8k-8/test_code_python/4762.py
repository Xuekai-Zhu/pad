def solution():
    # Calculate the area of each TV screen in square inches
    bill_screen_area = 48 * 100
    bob_screen_area = 70 * 60

    # Calculate the weight of each TV in ounces
    bill_weight = bill_screen_area * 4
    bob_weight = bob_screen_area * 4

    # Convert the weight of each TV to pounds
    bill_weight_lb = bill_weight / 16
    bob_weight_lb = bob_weight / 16

    # Calculate the difference in weight between the two TVs in pounds
    weight_diff = bob_weight_lb - bill_weight_lb
    result = weight_diff
    return result

print(solution())