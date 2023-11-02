def solution():
    """Bill gets a flat-screen TV that measures 48 inches by 100 inches. His brother Bob gets a TV that measures 70 inches by 60 inches. If the TVs weigh 4 oz per square inch of screen space, how much more does the heavier TV weigh in pounds? (There are 16 ounces per pound)."""
    bill_screen_space = 48 * 100
    bob_screen_space = 70 * 60
    weight_per_screen_space = 4 / 16 # converting from ounces to pounds
    bill_weight = bill_screen_space * weight_per_screen_space
    bob_weight = bob_screen_space * weight_per_screen_space
    weight_difference = bob_weight - bill_weight
    result = weight_difference
    return result

print(solution())