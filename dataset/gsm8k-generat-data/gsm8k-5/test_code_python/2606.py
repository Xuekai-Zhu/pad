def solution():
    num_students = 35  # There are 35 students in the class
    num_chaperones = 4  # There are 4 adult chaperones
    student_fee = 5  # The entrance fee for students is $5
    chaperone_fee = 6  # The entrance fee for chaperones is $6

    # Calculate the total cost for student entrance fees
    student_cost = num_students * student_fee

    # Calculate the total cost for chaperone entrance fees
    chaperone_cost = num_chaperones * chaperone_fee

    # Calculate the total entrance fee cost
    total_cost = student_cost + chaperone_cost
    result = total_cost
    return result

print(solution())