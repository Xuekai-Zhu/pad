def solution():
    total_contribution = 90  # Each class will contribute $90
    class_funds = 14  # Miss Evans' class has $14 in class funds
    remaining_contribution = total_contribution - (class_funds / 19)  # The remaining contribution after using class funds

    # Calculate how much each student will contribute
    each_student_contribution = remaining_contribution / 19
    result = each_student_contribution
    return result

print(solution())