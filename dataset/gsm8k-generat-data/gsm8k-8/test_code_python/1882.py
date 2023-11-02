def solution():
    # Calculate the number of bananas left on the tree after Raj cut some
    bananas_left_on_tree = 100

    # Calculate the number of bananas Raj initially took from the tree
    initial_bananas_taken = bananas_left_on_tree + 70

    # Calculate the number of bananas remaining in Raj's basket
    bananas_in_basket = initial_bananas_taken * 2

    # Calculate the total number of bananas initially on the tree
    total_bananas_initially = bananas_left_on_tree + initial_bananas_taken + bananas_in_basket
    result = total_bananas_initially
    return result

print(solution())