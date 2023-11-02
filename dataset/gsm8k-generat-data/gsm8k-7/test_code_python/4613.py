def solution():
    num_students = 30
    contribution_per_student = 2
    num_fridays = 8  # 2 months (60 days) with 7 Fridays each plus additional Fridays

    # Calculate the total amount contributed by all students
    total_contribution = num_students * contribution_per_student * num_fridays

    result = total_contribution
    return result

print(solution())