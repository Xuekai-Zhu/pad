def solution():
    
    num_students = 40
    cookies_per_student = 2
    oatmeal_raisin_percent = 0.1
    oatmeal_raisin_cookies = int(num_students * oatmeal_raisin_percent) * cookies_per_student
    result = oatmeal_raisin_cookies
    return result

print(solution())