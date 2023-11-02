def solution():
    """The teacher agrees to order pizza for the class. For every student in the class, she will buy 2 pieces of cheese and 1 piece of onion and they will eat exactly that amount. A large pizza has 18 slices. She orders 6 total pizzas and there are 8 pieces of cheese and 4 pieces of onion leftover. How many students are in the class?"""
    # Define the number of pizzas ordered
    pizzas_ordered = 6

    # Calculate the total number of pizza slices ordered
    total_slices = pizzas_ordered * 18

    # Calculate the total number of cheese and onion slices ordered
    cheese_slices = total_slices - 8
    onion_slices = total_slices - 4

    # Calculate the number of students in the class
    # Since for every student there are 2 cheese slices and 1 onion slice,
    # we can set up the following equation:
    # 2x + x = cheese_slices + onion_slices
    # where x is the number of students in the class
    x = (cheese_slices + onion_slices) / 3

    result = round(x)
    return result

print(solution())