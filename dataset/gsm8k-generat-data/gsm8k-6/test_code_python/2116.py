def solution():
    # Calculate the total number of sales and the number of sales on each street
    total_sales = 175 / 25  # Rodney gets $25 for each system he sells
    third_street_sales = 0  # all houses on the third street turned him away
    fourth_street_sales = 1  # fourth street resulted in only one sale
    second_street_sales = 2 * (first_street_sales := fourth_street_sales)  # the first street sales are half of the second street sales

    # Calculate the total number of sales on all streets except the third street
    total_sales_except_third = first_street_sales + second_street_sales + fourth_street_sales

    # Calculate the number of sales on the second street
    second_street_sales = total_sales - total_sales_except_third

    result = second_street_sales
    return result

print(solution())