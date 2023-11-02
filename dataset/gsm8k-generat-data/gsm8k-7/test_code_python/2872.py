def solution():
    num_students = 40
    cookies_per_student = 2
    oatmeal_raisin_percent = 0.1

    # Calculate the total number of cookies needed
    total_cookies = num_students * cookies_per_student

    # Calculate the number of oatmeal raisin cookies
    oatmeal_raisin_cookies = total_cookies * oatmeal_raisin_percent

    result = oatmeal_raisin_cookies
    return result

print(solution())