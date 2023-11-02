def solution():
    """Big boxes contain 7 dolls each. Small boxes contain 4 dolls each. There are 5 big boxes and 9 small boxes. How many dolls are there in total?"""
    # Define the number of dolls per big box and small box
    BIG_BOX_DOLLS = 7
    SMALL_BOX_DOLLS = 4

    # Define the number of big boxes and small boxes
    big_boxes = 5
    small_boxes = 9

    # Calculate the total number of dolls
    total_dolls = (BIG_BOX_DOLLS * big_boxes) + (SMALL_BOX_DOLLS * small_boxes)

    # Display the total number of dolls
    result = total_dolls
    return result

print(solution())