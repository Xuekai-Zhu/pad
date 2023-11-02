def solution():
    """Sonny received 45 boxes of cookies from his friend yesterday. He gave 12 to his brother, 9 to his sister, and he gave 7 to his cousin. How many boxes of cookies were left for him?"""
    # Define the number of boxes given to each family member
    brother_boxes = 12
    sister_boxes = 9
    cousin_boxes = 7

    # Calculate the total boxes given away
    total_given = brother_boxes + sister_boxes + cousin_boxes

    # Calculate the number of boxes left for Sonny
    left_boxes = 45 - total_given

    # Display the number of boxes left for Sonny
    result = left_boxes
    return result

print(solution())