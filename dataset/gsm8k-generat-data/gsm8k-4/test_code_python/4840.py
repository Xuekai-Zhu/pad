def solution():
    """Noel bakes 4 dozen donuts for his class. There are 30 students in class, but only 80% like donuts. How many donuts does each student who likes donuts get to eat?"""
    # Define the number of donuts baked and the number of students
    donuts = 4 * 12
    students = 30

    # Calculate the number of students who like donuts
    like_donuts = int(students * 0.8)

    # Calculate the number of donuts each student who likes donuts gets to eat
    donuts_per_student = donuts // like_donuts

    # return the result
    result = donuts_per_student
    return result

print(solution())