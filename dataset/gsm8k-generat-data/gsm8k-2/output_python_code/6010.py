def solution():
    """Mr. Gardner bakes 20 cookies, 25 cupcakes, and 35 brownies for his second-grade class of 20 students. If he wants to give each student an equal amount of sweet treats, how many sweet treats will each student receive?"""
    total_sweets = 20 + 25 + 35
    total_students = 20
    sweets_per_student = total_sweets // total_students
    result = sweets_per_student
    return result

print(solution())