def solution():
    # Find the number of students who receive $6 allowance
    num_six_allowance = (2/3) * 60

    # Find the total amount of money received by students who get $6 allowance
    total_six_allowance = num_six_allowance * 6

    # Find the total amount of money received by students who get $4 allowance
    num_four_allowance = 60 - num_six_allowance
    total_four_allowance = num_four_allowance * 4

    # Find the total amount of money received by all students
    total_allowance = total_six_allowance + total_four_allowance
    result = total_allowance
    return result

print(solution())