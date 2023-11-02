def solution():
    katya_sales = 8  # Katya sold 8 glasses of lemonade
    ricky_sales = 9  # Ricky sold 9 glasses of lemonade
    combined_sales = katya_sales + ricky_sales  # Combined sales of Katya and Ricky

    tina_sales = 2 * combined_sales  # Tina sold twice as many as Katya and Ricky's combined sales
    difference = tina_sales - katya_sales  # Calculate the difference between Tina's and Katya's sales

    result = difference
    return result

print(solution())