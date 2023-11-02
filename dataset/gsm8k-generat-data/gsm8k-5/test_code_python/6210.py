def solution():
    pieces_per_pizza = 6  # Doc's Pizza contains 6 pieces of pizza
    num_students = 10  
    num_pizzas_per_student = 20  
    num_pizzas_total = num_students * num_pizzas_per_student  # Total number of pizzas ordered by all students
    num_pieces_total = pieces_per_pizza * num_pizzas_total  # Total number of pieces of pizza carried by all students

    result = num_pieces_total
    return result

print(solution())