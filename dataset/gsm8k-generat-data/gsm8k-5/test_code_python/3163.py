def solution():
    slices_per_pizza = 18  # A large pizza has 18 slices
    num_pizzas = 6  # The teacher orders 6 pizzas
    total_slices = slices_per_pizza * num_pizzas  # Calculate the total number of pizza slices

    cheese_leftover = 8  # There are 8 pieces of cheese leftover
    onion_leftover = 4  # There are 4 pieces of onion leftover
    slices_per_student = 2 * 2 + 1  # Each student eats 2 pieces of cheese and 1 piece of onion

    # Calculate the number of students in the class
    num_students = (total_slices - cheese_leftover - onion_leftover) / slices_per_student
    result = num_students
    return result

print(solution())