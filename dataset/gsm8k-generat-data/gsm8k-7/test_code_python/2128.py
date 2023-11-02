def solution():
    num_students = 200
    cups_per_student = 10
    cups_per_jug = 40

    # Calculate the total cups of water needed
    total_cups = num_students * cups_per_student

    # Calculate the total jugs needed
    total_jugs = total_cups / cups_per_jug

    result = total_jugs
    return result

print(solution())