def solution():
    """Doc's Pizza contains 6 pieces of pizza. Ten fourth-graders each bought 20 pizzas from Doc's Pizza and put them in their box. How many pieces of pizza are the children carrying in total?"""
    # Define the number of pieces of pizza in one box
    PIZZA_PER_BOX = 6

    # Define the number of boxes bought by each fourth-grader
    BOXES_PER_STUDENT = 20

    # Calculate the number of pieces of pizza each student is carrying
    pieces_per_student = PIZZA_PER_BOX * BOXES_PER_STUDENT

    # Calculate the total number of pieces of pizza carried by all the students
    total_pieces = pieces_per_student * 10

    # Display the total number of pieces of pizza
    result = total_pieces
    return result

print(solution())