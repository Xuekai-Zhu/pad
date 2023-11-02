def solution():
    """Dani brings two and half dozen cupcakes for her 2nd-grade class. There are 27 students (including Dani), 1 teacher, and 1 teacher’s aid. If 3 students called in sick that day, how many cupcakes are left after Dani gives one to everyone in the class?"""
    # Define the initial number of cupcakes brought by Dani
    initial_cupcakes = 2.5 * 12

    # Define the total number of people in the class
    total_people = 27 + 1 + 1

    # Subtract the number of sick students
    total_people -= 3

    # Subtract one cupcake for each person in the class
    remaining_cupcakes = initial_cupcakes - total_people

    # Display the number of remaining cupcakes
    result = remaining_cupcakes
    return result

print(solution())