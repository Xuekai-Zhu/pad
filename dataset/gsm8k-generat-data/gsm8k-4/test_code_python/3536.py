def solution():
    """Katya sold 8 glasses of lemonade and Ricky sold 9 glasses of lemonade. If Tina sold twice as many as Katya and Ricky's combined sales, how many more glasses of lemonade than Katya did Tina sell?"""
    # Define the number of glasses sold by Katya and Ricky
    katya_sales = 8
    ricky_sales = 9

    # Calculate the combined sales of Katya and Ricky
    combined_sales = katya_sales + ricky_sales

    # Calculate the number of glasses sold by Tina
    tina_sales = combined_sales * 2

    # Calculate the difference in sales between Tina and Katya
    difference = tina_sales - katya_sales

    # return the result
    result = difference
    return result

print(solution())