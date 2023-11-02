def solution():
    """Doc's Pizza contains 6 pieces of pizza. Ten fourth-graders each bought 20 pizzas from Doc's Pizza and put them in their box. How many pieces of pizza are the children carrying in total?"""
    pieces_per_box = 6
    num_students = 10
    num_boxes = 20
    total_pieces = pieces_per_box * num_students * num_boxes
    result = total_pieces
    return result

print(solution())