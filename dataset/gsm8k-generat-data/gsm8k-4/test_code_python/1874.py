def solution():
    """Sonny received 45 boxes of cookies from his friend yesterday. He gave 12 to his brother, 9 to his sister, and he gave 7 to his cousin. How many boxes of cookies were left for him?"""
    # Define the initial number of boxes of cookies
    initial_boxes = 45

    # Define the number of boxes given to Sonny's family members
    family_boxes = 12 + 9 + 7

    # Calculate the remaining number of boxes
    remaining_boxes = initial_boxes - family_boxes

    # return the result
    result = remaining_boxes
    return result

print(solution())