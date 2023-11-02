def solution():
    # Define the variables
    class_size = 10
    merged_class_size = 10
    num_chaperones = 5
    num_teachers = 2
    num_students_left = 10
    num_chaperones_left = 2

    # Calculate the total number of individuals at the zoo
    total_individuals = class_size + merged_class_size + num_chaperones + num_teachers

    # Subtract the number of individuals who left
    total_individuals -= (num_students_left + num_chaperones_left)

    result = total_individuals
    return result

print(solution())