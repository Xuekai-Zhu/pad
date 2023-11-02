def solution():
    # Define the number of donuts baked by Noel
    donuts = 4 * 12

    # Calculate the number of students who like donuts
    students_like_donuts = round(0.8 * 30)

    # Calculate the number of donuts each student who likes donuts gets to eat
    donuts_per_student = donuts // students_like_donuts
    result = donuts_per_student
    return result

print(solution())