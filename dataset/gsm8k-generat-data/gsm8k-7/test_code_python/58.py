def solution():
    num_students = 60
    frac_six = 2/3
    frac_four = 1 - frac_six
    six_avg = 6
    four_avg = 4

    #Calculate the number of students that receive $6 allowance
    num_six = frac_six * num_students

    # Calculate the number of students that receive $4 allowance
    num_four = frac_four * num_students

    # Calculate the total amount of money received by students who receive $6 allowance
    total_six = num_six * six_avg

    # Calculate the total amount of money received by students who receive $4 allowance
    total_four = num_four * four_avg

    # Calculate the total amount of money received by all students
    total_money = total_six + total_four
    result = total_money
    return result

print(solution())