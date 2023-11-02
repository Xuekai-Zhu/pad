def solution():
    num_classes = 4
    num_students_per_class = 30
    num_students_pe = 50

    # Calculate the total number of cupcakes needed for the fourth-grade classes
    cupcakes_for_classes = num_classes * num_students_per_class

    # Calculate the total number of cupcakes needed for the P.E. class
    cupcakes_for_pe = num_students_pe

    # Calculate the total number of cupcakes needed
    total_cupcakes_needed = cupcakes_for_classes + cupcakes_for_pe
    result = total_cupcakes_needed
    return result

print(solution())