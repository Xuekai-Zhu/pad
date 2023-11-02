def solution():
    total_cookies = 20
    total_cupcakes = 25
    total_brownies = 35
    total_students = 20
    total_treats = total_cookies + total_cupcakes + total_brownies
    treats_per_student = total_treats / total_students
    result = treats_per_student
    return result

print(solution())