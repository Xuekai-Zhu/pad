def solution():
    """The teacher agrees to order pizza for the class. For every student in the class, she will buy 2 pieces of cheese and 1 piece of onion and they will eat exactly that amount. A large pizza has 18 slices. She orders 6 total pizzas and there are 8 pieces of cheese and 4 pieces of onion leftover. How many students are in the class?"""
    cheese_per_student = 2
    onion_per_student = 1
    total_slices_per_pizza = 18
    leftover_cheese = 8
    leftover_onion = 4
    total_pizzas = 6
    total_slices_ordered = total_pizzas * total_slices_per_pizza
    total_cheese_ordered = total_slices_ordered // cheese_per_student
    total_onion_ordered = total_slices_ordered // onion_per_student
    students = min(total_cheese_ordered - leftover_cheese, total_onion_ordered - leftover_onion)
    result = students
    return result

print(solution())