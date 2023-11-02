def solution():
    """Balki is counting the number of raisins in boxes of cereal. He counted 437 total raisins in 5 boxes. In one box he counted 72 raisins. In a second box he counted 74 raisins. The other three boxes had the same number each. How many were in each of the other three boxes?"""
    # Define the total number of raisins and the number of raisins in the first two boxes
    total_raisins = 437
    raisins_1 = 72
    raisins_2 = 74

    # Calculate the sum of raisins in the other three boxes
    other_boxes_sum = total_raisins - raisins_1 - raisins_2

    # Calculate the number of raisins in each of the other three boxes
    other_boxes = other_boxes_sum / 3

    # Display the number of raisins in each of the other three boxes
    result = other_boxes
    return result

print(solution())