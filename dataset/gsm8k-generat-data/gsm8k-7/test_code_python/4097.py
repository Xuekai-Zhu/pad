def solution():
    total_students = 400
    tree_huggers = 120
    poets = tree_huggers + 50

    # Calculate the total number of poets and treehuggers
    total_p_and_t = poets + tree_huggers

    # Calculate the number of singers
    singers = total_students - total_p_and_t

    result = singers
    return result

print(solution())