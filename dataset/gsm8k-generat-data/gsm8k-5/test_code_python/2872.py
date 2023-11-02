def solution():
    total_students = 40  # There are 40 students in Giorgio's class
    cookies_per_student = 2  # Giorgio plans to make 2 cookies per student

    oatmeal_raisin_percentage = 0.1  # 10% of classmates want oatmeal raisin cookies
    oatmeal_raisin_cookies = int(total_students * oatmeal_raisin_percentage * cookies_per_student)

    result = oatmeal_raisin_cookies
    return result

print(solution())