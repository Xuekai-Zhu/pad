def solution():
    """Dani brings two and half dozen cupcakes for her 2nd-grade class. There are 27 students (including Dani), 1 teacher, and 1 teacher’s aid. If 3 students called in sick that day, how many cupcakes are left after Dani gives one to everyone in the class?"""
    # Define the number of cupcakes Dani brings
    CUPCAKES = 30

    # Define the number of students, teacher, and teacher's aid
    PEOPLE = 29

    # Define the number of students who called in sick
    SICK_STUDENTS = 3

    # Calculate the number of cupcakes needed
    cupcakes_needed = PEOPLE - SICK_STUDENTS

    # Subtract the cupcakes needed from the total number of cupcakes
    cupcakes_left = CUPCAKES - cupcakes_needed

    # Display the number of cupcakes left
    result = cupcakes_left
    return result

print(solution())