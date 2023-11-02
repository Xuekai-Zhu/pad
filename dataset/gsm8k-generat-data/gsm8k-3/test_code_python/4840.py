def solution():
    """Noel bakes 4 dozen donuts for his class. There are 30 students in class, but only 80% like donuts. How many donuts does each student who likes donuts get to eat?"""
    # Define the number of donuts baked
    donuts_baked = 4 * 12

    # Define the number of students who like donuts
    students_like_donuts = int(30 * 0.8)

    # Calculate the number of donuts each student who likes donuts gets to eat
    donuts_per_student = donuts_baked // students_like_donuts

    # Display the number of donuts each student who likes donuts gets to eat
    result = donuts_per_student
    return result

print(solution())