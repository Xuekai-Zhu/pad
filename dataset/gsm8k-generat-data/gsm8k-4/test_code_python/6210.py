def solution():
    """Doc's Pizza contains 6 pieces of pizza. Ten fourth-graders each bought 20 pizzas from Doc's Pizza and put them in their box. How many pieces of pizza are the children carrying in total?"""
    # Define the number of pizza pieces per box and the number of boxes purchased by each fourth-grader
    PIZZA_PER_BOX = 6
    BOXES_PER_FOURTH_GRADER = 20

    # Calculate the total number of pizza pieces purchased by all fourth-graders
    total_boxes = 10 * BOXES_PER_FOURTH_GRADER
    total_pieces = total_boxes * PIZZA_PER_BOX

    # return the result
    result = total_pieces
    return result

print(solution())