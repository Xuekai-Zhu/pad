def solution():
    """Bill gets a flat-screen TV that measures 48 inches by 100 inches. His brother Bob gets a TV that measures 70 inches by 60 inches. If the TVs weigh 4 oz per square inch of screen space, how much more does the heavier TV weigh in pounds?"""
    bill_screen_space = 48 * 100
    bob_screen_space = 70 * 60
    bill_weight = bill_screen_space * 4
    bob_weight = bob_screen_space * 4
    weight_difference = bob_weight - bill_weight
    weight_difference_in_pounds = weight_difference / (16*oz_per_pound)
    
    result = weight_difference_in_pounds
    return result

print(solution())