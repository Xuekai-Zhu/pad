def solution():
    """Big boxes contain 7 dolls each. Small boxes contain 4 dolls each. There are 5 big boxes and 9 small boxes. How many dolls are there in total?"""
    # Define the number of dolls in each big and small box
    big_box_dolls = 7
    small_box_dolls = 4

    # Define the number of big and small boxes
    num_big_boxes = 5
    num_small_boxes = 9

    # Calculate the total number of dolls in the big boxes
    total_big_box_dolls = big_box_dolls * num_big_boxes

    # Calculate the total number of dolls in the small boxes
    total_small_box_dolls = small_box_dolls * num_small_boxes

    # Calculate the total number of dolls
    total_dolls = total_big_box_dolls + total_small_box_dolls

    # return the result
    result = total_dolls
    return result

print(solution())