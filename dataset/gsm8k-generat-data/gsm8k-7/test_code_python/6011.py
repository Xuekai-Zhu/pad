def solution():
    num_cookies = 20
    num_cupcakes = 25
    num_brownies = 35
    num_students = 20

    # Calculate the total number of sweet treats
    total_treats = num_cookies + num_cupcakes + num_brownies

    # Divide the total number of sweet treats by the number of students to get the number of treats per student
    treats_per_student = total_treats / num_students
    result = treats_per_student
    return result

print(solution())