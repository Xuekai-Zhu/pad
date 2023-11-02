def solution():
    num_box_type_1 = 50
    num_box_type_2 = 80
    num_box_type_3 = 70

    num_cookies_box_1 = 12
    num_cookies_box_2 = 20
    num_cookies_box_3 = 16

    # Calculate the total number of cookies sold for each type
    total_cookies_type_1 = num_box_type_1 * num_cookies_box_1
    total_cookies_type_2 = num_box_type_2 * num_cookies_box_2
    total_cookies_type_3 = num_box_type_3 * num_cookies_box_3

    # Calculate the total number of cookies sold
    total_cookies_sold = total_cookies_type_1 + total_cookies_type_2 + total_cookies_type_3
    result = total_cookies_sold
    return result

print(solution())