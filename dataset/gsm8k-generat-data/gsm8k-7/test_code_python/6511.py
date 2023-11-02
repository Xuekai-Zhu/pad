def solution():
    hoopit_toes_per_student = 3 * 4   # 3 toes on each of 4 hands
    neglart_toes_per_student = 2 * 5  # 2 toes on each of 5 hands
    num_hoopit_students = 7
    num_neglart_students = 8

    # Calculate the total number of toes on the school bus
    total_hoopit_toes = hoopit_toes_per_student * num_hoopit_students
    total_neglart_toes = neglart_toes_per_student * num_neglart_students
    total_toes = total_hoopit_toes + total_neglart_toes
    result = total_toes
    return result

print(solution())