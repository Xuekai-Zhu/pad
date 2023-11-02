def solution():
    # Calculate the total number of cupcakes brought by Dani
    total_cupcakes = 2.5 * 12  # two and half dozen cupcakes

    # Calculate the number of cupcakes needed for the class
    class_size = 27 - 3  # accounting for 3 sick students
    cupcakes_needed = class_size + 2 # adding Dani, teacher, and teacher's aid

    # Calculate the number of cupcakes left after giving one to each person
    cupcakes_left = total_cupcakes - cupcakes_needed + 1  # adding one for Dani

    result = cupcakes_left
    return result

print(solution())