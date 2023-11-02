def solution():
    total_students = 40
    cookies_per_student = 2
    oatmeal_raisin_percent = 10
    oatmeal_raisin_cookies = total_students * (oatmeal_raisin_percent / 100) * cookies_per_student
    result = oatmeal_raisin_cookies
    return result

print(solution())