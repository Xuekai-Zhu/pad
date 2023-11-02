def solution():
    """For a class fundraiser, 30 students were asked to bring in 12 brownies each. 20 students were asked to bring in 24 cookies each and 15 students were asked to bring in 12 donuts each. If they sell everything for $2.00 each, how much money will they raise?"""
    # Define the number of students and the number of baked goods each student brings
    brownies_per_student = 12
    cookies_per_student = 24
    donuts_per_student = 12

    # Define the number of students for each type of baked good
    brownie_students = 30
    cookie_students = 20
    donut_students = 15

    # Calculate the total number of each type of baked good
    total_brownies = brownie_students * brownies_per_student
    total_cookies = cookie_students * cookies_per_student
    total_donuts = donut_students * donuts_per_student

    # Calculate the total amount raised from each type of baked good
    brownie_sales = total_brownies * 2
    cookie_sales = total_cookies * 2
    donut_sales = total_donuts * 2

    # Calculate the total amount raised
    total_sales = brownie_sales + cookie_sales + donut_sales

    # return the result
    result = total_sales
    return result

print(solution())