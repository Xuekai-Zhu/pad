def solution():
    """Mr. Gardner bakes 20 cookies, 25 cupcakes, and 35 brownies for his second-grade class of 20 students. If he wants to give each student an equal amount of sweet treats, how many sweet treats will each student receive?"""
    # Define the number of students and the number of each type of sweet treat
    num_students = 20
    num_cookies = 20
    num_cupcakes = 25
    num_brownies = 35

    # Calculate the total number of sweet treats
    total_treats = num_cookies + num_cupcakes + num_brownies

    # Calculate the number of sweet treats per student
    treats_per_student = total_treats // num_students

    # Display the number of sweet treats per student
    result = treats_per_student
    return result

print(solution())