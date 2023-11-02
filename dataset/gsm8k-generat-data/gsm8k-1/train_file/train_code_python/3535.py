def solution():
    """Katya sold 8 glasses of lemonade and Ricky sold 9 glasses of lemonade.
    If Tina sold twice as many as Katya and Ricky's combined sales,
    how many more glasses of lemonade than Katya did Tina sell?"""
    
    katya_sales = 8
    ricky_sales = 9
    combined_sales = katya_sales + ricky_sales
    tina_sales = combined_sales * 2
    more_sales_than_katya = tina_sales - katya_sales
    result = more_sales_than_katya
    
    return result

print(solution())