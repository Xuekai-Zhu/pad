def solution():
    cupcakes_per_dozen = 12  # There are 12 cupcakes in a dozen
    cupcakes_per_student = 1  # Dani gives one cupcake to each student
    total_students = 27  # There are 27 students (including Dani), 1 teacher, and 1 teacher's aid
    total_sick_students = 3  # Three students called in sick that day

    # Calculate the total number of cupcakes Dani brings
    total_cupcakes = 2.5 * cupcakes_per_dozen

    # Calculate the number of cupcakes given to the class
    cupcakes_given = (total_students - total_sick_students) * cupcakes_per_student

    # Calculate the number of cupcakes left
    cupcakes_left = total_cupcakes - cupcakes_given
    result = cupcakes_left
    return result

print(solution())