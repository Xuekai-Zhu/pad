def solution():
    commission_per_sale = 25  # Rodney gets $25 commission per sale
    total_commission = 175  # Rodney's total commission is $175
    total_houses = 4 * 8  # Rodney is canvassing 4 streets, each with 8 houses

    # Calculate the number of sales Rodney made on the first street
    first_street_sales = second_street_sales / 2
    
    # Calculate the number of sales Rodney made on the third street
    third_street_sales = 0

    # Calculate the number of sales Rodney made on the fourth street
    fourth_street_sales = 1
    
    # Calculate the total number of sales Rodney made
    total_sales = first_street_sales + second_street_sales + third_street_sales + fourth_street_sales
    
    # Calculate the number of sales Rodney made on the second street
    second_street_sales = (total_commission - (third_street_sales * commission_per_sale) - (fourth_street_sales * commission_per_sale) - (first_street_sales * commission_per_sale)) / commission_per_sale

    result = second_street_sales
    return result

print(solution())