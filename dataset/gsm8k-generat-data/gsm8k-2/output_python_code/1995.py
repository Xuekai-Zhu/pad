def solution():
    """Ali has a small flower shop. He sold 4 flowers on Monday, 8 flowers on Tuesday and on Friday, he sold double the number of flowers he sold on Monday. How many flowers does Ali sell?"""
    monday_sales = 4
    tuesday_sales = 8
    friday_sales = 2 * monday_sales
    total_sales = monday_sales + tuesday_sales + friday_sales
    result = total_sales
    return result

print(solution())