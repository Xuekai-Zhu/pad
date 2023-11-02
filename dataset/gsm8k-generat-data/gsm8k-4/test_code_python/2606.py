def solution():
    """Jessica’s class is going to a farm for a field trip. The school will bring all 35 students in the class plus 4 adult chaperones. The farm entrance fee for students costs $5 and $6 for adults. How much will the school pay for the farm entrance in all?"""
    # Define the number of students, adult chaperones, and their respective entrance fees
    num_students = 35
    num_chaperones = 4
    student_fee = 5
    chaperone_fee = 6

    # Calculate the total cost of entrance fees for students and adult chaperones
    total_cost = (num_students * student_fee) + (num_chaperones * chaperone_fee)

    result = total_cost
    return result

print(solution())