def solution():
    # Calculate the number of students receiving $6 allowance
    students_with_6dollars = 2/3 * 60
    # Calculate the amount of money received by students with $6 allowance
    money_from_6dollars_students = students_with_6dollars * 6
    # Calculate the number of students receiving $4 allowance
    students_with_4dollars = 60 - students_with_6dollars
    # Calculate the amount of money received by students with $4 allowance
    money_from_4dollars_students = students_with_4dollars * 4
    # Calculate the total amount of money received by all students
    total_money_received = money_from_6dollars_students + money_from_4dollars_students
    result = total_money_received
    return result

print(solution())