def solution():
    # Define the number of students and cookies per student
    num_students = 40
    cookies_per_student = 2

    # Calculate the total number of cookies
    total_cookies = num_students * cookies_per_student

    # Calculate the number of oatmeal raisin cookies, which is 10% of the total cookies
    oatmeal_cookies = total_cookies * 0.1

    result = oatmeal_cookies
    return result

print(solution())