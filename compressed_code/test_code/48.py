def solution():
    
    total_students = 60
    two_thirds = int(2/3 * total_students)
    remaining_students = total_students - two_thirds
    allowance_1 = 6
    allowance_2 = 4
    total_allowance_1 = two_thirds * allowance_1
    total_allowance_2 = remaining_students * allowance_2
    total_allowance = total_allowance_1 + total_allowance_2
    result = total_allowance
    return result

print(solution())