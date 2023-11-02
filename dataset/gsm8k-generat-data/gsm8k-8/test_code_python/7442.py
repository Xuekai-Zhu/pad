def solution():
    # Calculate the total cost of buying a reading book for each student
    per_student_cost = 12

    # Calculate the total cost of buying reading books for all the students
    total_cost = per_student_cost * 30

    # Check if the total cost is greater than the amount Sally was given
    if total_cost <= 320:
        sally_pays_out_of_pocket = 0
    else:
        sally_pays_out_of_pocket = total_cost - 320

    result = sally_pays_out_of_pocket
    return result

print(solution())