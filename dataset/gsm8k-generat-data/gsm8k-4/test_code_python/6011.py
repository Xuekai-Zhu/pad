def solution():
    """Mr. Gardner bakes 20 cookies, 25 cupcakes, and 35 brownies for his second-grade class of 20 students. If he wants to give each student an equal amount of sweet treats, how many sweet treats will each student receive?"""
    # Define the total number of sweet treats
    total_sweets = 20 + 25 + 35

    # Define the number of students
    num_students = 20

    # Calculate the number of sweet treats each student will receive
    sweets_per_student = total_sweets / num_students

    # Return the result
    result = sweets_per_student
    return result

print(solution())