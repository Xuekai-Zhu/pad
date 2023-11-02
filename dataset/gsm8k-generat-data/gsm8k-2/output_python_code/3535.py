def solution():
    """Katya sold 8 glasses of lemonade and Ricky sold 9 glasses of lemonade. If Tina sold twice as many as Katya and Ricky's combined sales, how many more glasses of lemonade than Katya did Tina sell?"""
    katya_sales = 8
    ricky_sales = 9
    combined_sales = katya_sales + ricky_sales
    tina_sales = 2 * combined_sales
    difference = tina_sales - katya_sales
    result = difference
    return result

print(solution())