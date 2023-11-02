def solution():
    pieces_per_pizza = 6
    num_students = 10
    num_pizzas_per_student = 20

    # Calculate the total number of pizzas bought by all students
    total_num_pizzas = num_students * num_pizzas_per_student

    # Calculate the total number of pizza pieces
    total_num_pieces = total_num_pizzas * pieces_per_pizza
    result = total_num_pieces
    return result

print(solution())