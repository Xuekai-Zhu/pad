def solution():
    num_students_1 = (2/3) * 60  # Number of students receiving $6 per day
    num_students_2 = (1/3) * 60  # Number of students receiving $4 per day

    # Calculate the total amount of money the students with $6 allowance receive per day
    total_money_1 = num_students_1 * 6

    # Calculate the total amount of money the students with $4 allowance receive per day
    total_money_2 = num_students_2 * 4

    # Calculate the total amount of money all the students receive per day
    total_money = total_money_1 + total_money_2
    result = total_money
    return result

print(solution())