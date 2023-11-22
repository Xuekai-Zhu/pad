def solution():
    
    # Define the initial number of vanilla scents and fruity scents
    vanilla_scents = 4
    fruity_scents = 8

    # Calculate the number of vanilla scents and fruity scents sold
    vanilla_sales = vanilla_scents * 5
    fruity_sales = fruity_scents * 2

    # Calculate the difference in sales between the vanilla and fruity scents
    sales_difference = vanilla_sales - fruity_sales

    # return the result
    result = sales_difference
    return result

print(solution())