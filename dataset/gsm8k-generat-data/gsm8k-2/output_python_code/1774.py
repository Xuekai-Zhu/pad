def solution():
    """One student on a field trip counted 12 squirrels. Another counted a third more squirrels than the first student. How many squirrels did both students count combined?"""
    first_student_squirrels = 12
    second_student_squirrels = first_student_squirrels + (1/3 * first_student_squirrels)
    total_squirrels = first_student_squirrels + second_student_squirrels
    result = total_squirrels
    return result

print(solution())