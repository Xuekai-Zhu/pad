def solution():
    
    brownies_per_student = 12
    num_brownie_students = 30
    total_brownies = brownies_per_student * num_brownie_students

    cookies_per_student = 24
    num_cookie_students = 20
    total_cookies = cookies_per_student * num_cookie_students

    donuts_per_student = 12
    num_donut_students = 15
    total_donuts = donuts_per_student * num_donut_students

    total_items = total_brownies + total_cookies + total_donuts
    price_per_item = 2.00
    total_money_raised = total_items * price_per_item
    result = total_money_raised
    
    return result

print(solution())