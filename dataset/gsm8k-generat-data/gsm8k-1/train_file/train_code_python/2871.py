def solution():
    """Giorgio plans to make cookies for his class. There are 40 students and he plans to make 2 cookies per student. If 10% of his classmates want oatmeal raisin, then how many oatmeal raisin cookies will Giorgio make?"""
    num_students = 40
    cookies_per_student = 2
    oatmeal_raisin_percent = 0.1
    oatmeal_raisin_cookies = int(num_students * oatmeal_raisin_percent) * cookies_per_student
    result = oatmeal_raisin_cookies
    return result

print(solution())