def solution():
    """Giorgio plans to make cookies for his class. There are 40 students and he plans to make 2 cookies per student. If 10% of his classmates want oatmeal raisin, then how many oatmeal raisin cookies will Giorgio make?"""
    # Define the number of students and cookies per student
    num_students = 40
    cookies_per_student = 2

    # Calculate the total number of cookies
    total_cookies = num_students * cookies_per_student

    # Calculate the number of oatmeal raisin cookies
    oatmeal_raisin_cookies = round(total_cookies * 0.1)

    # Display the number of oatmeal raisin cookies
    result = oatmeal_raisin_cookies
    return result

print(solution())