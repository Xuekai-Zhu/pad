def solution():
    """With 82 students, there are 2 students for each computer. If there are 16 more students, how many computers must they have in total to continue with 2 students per computer?"""
    initial_students = 82
    initial_computers = initial_students // 2
    final_students = initial_students + 16
    final_computers = final_students // 2
    result = final_computers
    return result

print(solution())