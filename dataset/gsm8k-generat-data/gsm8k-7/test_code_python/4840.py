def solution():
    num_donuts = 4 * 12  # 4 dozen donuts
    num_students = 30
    percentage_liking_donuts = 0.8

    # Calculate the number of students who like donuts
    num_students_liking_donuts = int(num_students * percentage_liking_donuts)

    # Calculate the number of donuts each student who likes donuts gets to eat
    num_donuts_per_student = num_donuts // num_students_liking_donuts
    result = num_donuts_per_student
    return result

print(solution())