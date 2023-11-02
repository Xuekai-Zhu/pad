def solution():
    """The teacher agrees to order pizza for the class. For every student in the class, she will buy 2 pieces of cheese and 1 piece of onion and they will eat exactly that amount. A large pizza has 18 slices. She orders 6 total pizzas and there are 8 pieces of cheese and 4 pieces of onion leftover. How many students are in the class?"""
    # Define the number of slices per pizza
    SLICES_PER_PIZZA = 18

    # Define the number of leftover cheese and onion pieces
    LEFTOVER_CHEESE = 8
    LEFTOVER_ONION = 4

    # Calculate the total number of cheese and onion pieces needed for the class
    needed_cheese = 2 * (SLICES_PER_PIZZA * 6) - LEFTOVER_CHEESE
    needed_onion = 1 * (SLICES_PER_PIZZA * 6) - LEFTOVER_ONION

    # Calculate the number of students in the class
    num_students = min(needed_cheese // 2, needed_onion // 1)

    # Display the number of students in the class
    result = num_students
    return result

print(solution())