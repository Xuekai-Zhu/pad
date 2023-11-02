def solution():
    """Doc's Pizza contains 6 pieces of pizza. Ten fourth-graders each bought 20 pizzas from Doc's Pizza and put them in their box. How many pieces of pizza are the children carrying in total?"""
    pizza_per_box = 6
    num_students = 10
    num_pizzas_per_student = 20
    total_pizzas = pizza_per_box * num_pizzas_per_student * num_students
    total_pieces = total_pizzas * 6
    result = total_pieces
    return result

print(solution())