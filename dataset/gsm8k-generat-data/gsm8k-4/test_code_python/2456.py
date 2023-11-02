def solution():
    """Balki is counting the number of raisins in boxes of cereal. He counted 437 total raisins in 5 boxes. In one box he counted 72 raisins. In a second box he counted 74 raisins. The other three boxes had the same number each. How many were in each of the other three boxes?"""
    # Define the total number of raisins and the number of raisins in the first two boxes
    total_raisins = 437
    first_box_raisins = 72
    second_box_raisins = 74

    # Calculate the total number of raisins in the other three boxes
    other_boxes_raisins = total_raisins - first_box_raisins - second_box_raisins

    # Calculate the number of raisins in each of the other three boxes
    other_three_boxes_raisins = other_boxes_raisins / 3

    # Return the result
    result = other_three_boxes_raisins
    return result

print(solution())