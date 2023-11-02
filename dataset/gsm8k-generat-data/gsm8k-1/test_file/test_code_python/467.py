def solution():
    """There are 30 students in Marissa’s class. Each student started the year with 10 pencils. After two months, 1/5 of the total pencils in class were used. At the end of the year, only 1/3 of the remaining pencils were left. How many pencils were left?"""
    num_students = 30
    pencils_per_student = 10
    total_pencils = num_students * pencils_per_student
    used_pencils = total_pencils // 5
    remaining_pencils = total_pencils - used_pencils
    final_pencils = remaining_pencils // 3
    result = final_pencils
    return result

print(solution())