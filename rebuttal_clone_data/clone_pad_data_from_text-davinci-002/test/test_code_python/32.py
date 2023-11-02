def solution():
    
    surveyed_students = 60
    two_thirds_students = (2/3) * surveyed_students
    one_third_students = surveyed_students - two_thirds_students
    average_allowance_two_thirds = 6
    average_allowance_one_third = 4
    total_money = (two_thirds_students * average_allowance_two_thirds) + (one_third_students * average_allowance_one_third)
    result = total_money

    return result

print(solution())