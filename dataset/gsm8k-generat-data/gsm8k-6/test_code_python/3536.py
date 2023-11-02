def solution():
    # Calculate the total number of glasses of lemonade sold by Katya and Ricky
    katya_sales = 8
    ricky_sales = 9
    combined_sales = katya_sales + ricky_sales

    # Calculate the number of glasses of lemonade sold by Tina
    tina_sales = 2 * combined_sales

    # Calculate the difference in sales between Tina and Katya
    difference = tina_sales - katya_sales

    result = difference
    return result

print(solution())