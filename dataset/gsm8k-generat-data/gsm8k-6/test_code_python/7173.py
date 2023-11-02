def solution():
    # Calculate the number of students accepted and attending Harvard University
    accepted_students = 0.05 * 20000  # 5% of the 20,000 students who applied are accepted
    attending_students = 0.9 * accepted_students  # 90% of the accepted students choose to attend Harvard University
    result = attending_students
    return result

print(solution())