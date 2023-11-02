def solution():
    num_students_brownies = 30
    num_brownies_per_student = 12

    num_students_cookies = 20
    num_cookies_per_student = 24

    num_students_donuts = 15
    num_donuts_per_student = 12

    price_per_item = 2.0

    # Calculate the total number of brownies brought in
    total_brownies = num_students_brownies * num_brownies_per_student

    # Calculate the total number of cookies brought in
    total_cookies = num_students_cookies * num_cookies_per_student

    # Calculate the total number of donuts brought in
    total_donuts = num_students_donuts * num_donuts_per_student

    # Calculate the total number of items brought in
    total_items = total_brownies + total_cookies + total_donuts

    # Calculate the total amount of money raised
    total_money_raised = total_items * price_per_item
    result = total_money_raised
    return result

print(solution())