def solution():
    """Jessica’s class is going to a farm for a field trip. The school will bring all 35 students in the class plus 4 adult chaperones. The farm entrance fee for students costs $5 and $6 for adults. How much will the school pay for the farm entrance in all?"""
    # Define the entrance fees
    STUDENT_FEE = 5
    ADULT_FEE = 6

    # Define the number of students and chaperones
    students = 35
    chaperones = 4

    # Calculate the total cost for students and chaperones
    student_cost = students * STUDENT_FEE
    chaperone_cost = chaperones * ADULT_FEE

    # Calculate the total cost for the entrance fees
    total_cost = student_cost + chaperone_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())