def solution():
    """Bill gets a flat-screen TV that measures 48 inches by 100 inches. His brother Bob gets a TV that measures 70 inches by 60 inches. If the TVs weigh 4 oz per square inch of screen space, how much more does the heavier TV weigh in pounds? (There are 16 ounces per pound)."""
    # Calculate the total screen space of each TV
    bill_screen_space = 48 * 100
    bob_screen_space = 70 * 60

    # Calculate the weight of each TV in ounces
    bill_weight = bill_screen_space * 4
    bob_weight = bob_screen_space * 4

    # Calculate the difference in weight in ounces
    weight_diff = bob_weight - bill_weight

    # Convert the weight difference to pounds
    pound_diff = weight_diff / 16

    # Return the weight difference in pounds
    result = pound_diff
    return result

print(solution())