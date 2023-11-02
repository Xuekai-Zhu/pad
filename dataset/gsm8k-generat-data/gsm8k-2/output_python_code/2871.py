def solution():
    """Giorgio plans to make cookies for his class. There are 40 students and he plans to make 2 cookies per student. If 10% of his classmates want oatmeal raisin, then how many oatmeal raisin cookies will Giorgio make?"""
    total_students = 40
    oatmeal_percentage = 0.1
    oatmeal_students = total_students * oatmeal_percentage
    oatmeal_cookies = oatmeal_students * 2
    result = oatmeal_cookies
    return result

print(solution())