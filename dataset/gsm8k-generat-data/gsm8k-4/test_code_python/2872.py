def solution():
    """Giorgio plans to make cookies for his class. There are 40 students and he plans to make 2 cookies per student. If 10% of his classmates want oatmeal raisin, then how many oatmeal raisin cookies will Giorgio make?"""
    # Define the number of students and cookies per student
    students = 40
    cookies_per_student = 2

    # Calculate the total number of cookies to be made
    total_cookies = students * cookies_per_student

    # Calculate the number of oatmeal raisin cookies to be made
    oatmeal_raisin_percent = 0.1
    oatmeal_raisin_cookies = int(total_cookies * oatmeal_raisin_percent)

    # return the result
    result = oatmeal_raisin_cookies
    return result

print(solution())