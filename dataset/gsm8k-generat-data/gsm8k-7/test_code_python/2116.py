def solution():
    commission_per_sale = 25
    total_commission = 175

    # Calculate the total number of sales across all streets
    total_sales = total_commission / commission_per_sale

    # Calculate the number of sales on the fourth street
    sales_fourth_street = 1

    # Calculate the number of sales on the third street (0)
    sales_third_street = 0

    # Calculate the total number of sales on the first and second streets combined
    sales_first_second_street = total_sales - sales_third_street - sales_fourth_street

    # Calculate the ratio of sales on the first street to sales on the second street
    ratio_first_second_street = 1/2

    # Calculate the number of sales on the second street
    sales_second_street = sales_first_second_street / (1 + ratio_first_second_street)

    result = sales_second_street
    return result

print(solution())