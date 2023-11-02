def solution():
    # Calculate the total number of houses in the neighborhood
    total_houses = 4 * 8

    # Calculate the total commission Rodney earned
    total_commission = 175

    # Calculate the commission per house sold
    commission_per_sale = 25

    # Calculate the total number of systems sold
    total_sales = total_commission / commission_per_sale

    # Calculate the number of sales on the first and fourth streets
    sales_on_first_street = sales_on_fourth_street = total_sales / 2

    # Calculate the number of houses on the second and fourth streets
    houses_on_second_street = 8
    houses_on_third_street = 8
    houses_on_fourth_street = 8

    # Calculate the total number of sale on the second and fourth streets
    total_sales_on_second_and_fourth_streets = total_sales - sales_on_first_street

    # Calculate the number of sales on the fourth street
    sales_on_second_street = total_sales_on_second_and_fourth_streets - sales_on_fourth_street

    result = sales_on_second_street
    return result

print(solution())