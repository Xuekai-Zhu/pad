def solution():
    katya_sales = 8
    ricky_sales = 9

    # Calculate the combined sales of Katya and Ricky
    combined_sales = katya_sales + ricky_sales

    # Calculate Tina's sales, which is twice the combined sales of Katya and Ricky
    tina_sales = 2 * combined_sales

    # Calculate the difference between Tina's sales and Katya's sales
    difference = tina_sales - katya_sales

    result = difference
    return result

print(solution())