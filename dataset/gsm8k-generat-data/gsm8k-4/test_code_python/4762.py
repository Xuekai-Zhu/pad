def solution():
    """Bill gets a flat-screen TV that measures 48 inches by 100 inches. His brother Bob gets a TV that measures 70 inches by 60 inches. If the TVs weigh 4 oz per square inch of screen space, how much more does the heavier TV weigh in pounds? (There are 16 ounces per pound)."""
    # Define the dimensions of the TVs
    bill_length = 48
    bill_width = 100
    bob_length = 70
    bob_width = 60

    # Calculate the screen space of each TV
    bill_space = bill_length * bill_width
    bob_space = bob_length * bob_width

    # Calculate the weight of each TV
    bill_weight = bill_space * 4 / 16
    bob_weight = bob_space * 4 / 16

    # Calculate the weight difference in pounds
    weight_diff = (bob_weight - bill_weight) / 16

    # return the result
    result = weight_diff
    return result

print(solution())