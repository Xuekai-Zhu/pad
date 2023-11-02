def solution():
    """The teacher agrees to order pizza for the class. For every student in the class, she will buy 2 pieces of cheese and 1 piece of onion and they will eat exactly that amount. A large pizza has 18 slices. She orders 6 total pizzas and there are 8 pieces of cheese and 4 pieces of onion leftover. How many students are in the class?"""
    total_slices = 6 * 18
    cheese_slices = 8
    onion_slices = 4
    slices_eaten = cheese_slices + onion_slices
    slices_per_student = 2 + 1
    total_students = (total_slices - cheese_slices - onion_slices) // slices_per_student
    result = total_students
    return result

print(solution())